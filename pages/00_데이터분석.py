import streamlit as st
import altair as alt
import csv

st.set_page_config(page_title="MBTI 국가별 분포", page_icon="🌍", layout="centered")

# 📥 CSV 파일 불러오기 (업로드 없이 프로젝트 폴더에 있는 파일 사용)
@st.cache_data
def load_data():
    with open("countriesMBTI_16types.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

data = load_data()

# 🔤 MBTI 유형 목록 추출
mbti_types = [k for k in data[0].keys() if k != "Country"]

# 🧠 각 국가별 가장 높은 비율의 MBTI 유형 찾기
top_mbti_by_country = {}
for row in data:
    country = row["Country"]
    mbti_scores = {k: float(row[k]) for k in mbti_types}
    top_mbti = max(mbti_scores, key=mbti_scores.get)
    top_mbti_by_country[country] = top_mbti

# 📊 MBTI별로 최다 국가 수 계산
mbti_rank_count = {}
for mbti in mbti_types:
    mbti_rank_count[mbti] = sum(1 for c in top_mbti_by_country.values() if c == mbti)

# 📈 차트 데이터 정리
chart_data = [{"MBTI": k, "Country Count": v} for k, v in mbti_rank_count.items()]
chart_data = sorted(chart_data, key=lambda x: x["Country Count"], reverse=True)

# 🏷️ 제목 및 설명
st.title("🌍 국가별 MBTI 우세 유형 분석")
st.markdown("세계 각국에서 가장 비율이 높은 MBTI 유형은 무엇일까요?\nAltair 시각화를 통해 한눈에 살펴보세요.")

# 📊 Altair 막대그래프
chart = alt.Chart(alt.Data(values=chart_data)).mark_bar().encode(
    x=alt.X("MBTI:N", sort="-y", title="MBTI 유형"),
    y=alt.Y("Country Count:Q", title="가장 높은 비율로 나타난 국가 수"),
    color=alt.Color("MBTI:N", legend=None),
    tooltip=["MBTI:N", "Country Count:Q"]
).properties(
    width=600,
    height=400,
    title="🌐 각 MBTI 유형이 가장 우세한 국가 수"
)

# 차트 출력
st.altair_chart(chart, use_container_width=True)

# ℹ️ 하단 안내
st.markdown("---")
st.caption("📊 데이터: countriesMBTI_16types.csv | 시각화: Altair | 제작: Streamlit")
