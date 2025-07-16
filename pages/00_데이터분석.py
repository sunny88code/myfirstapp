import streamlit as st
import altair as alt
import csv

st.set_page_config(page_title="MBTI Top 3 분석", page_icon="🧠", layout="centered")

# 데이터 불러오기
@st.cache_data
def load_data():
    with open("countriesMBTI_16types.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

data = load_data()
mbti_types = [k for k in data[0].keys() if k != "Country"]

# 국가별 MBTI 상위 3 유형 추출
top3_data = []
top1_count = {}

for row in data:
    country = row["Country"]
    mbti_scores = {k: float(row[k]) for k in mbti_types}
    sorted_mbti = sorted(mbti_scores.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_mbti[:3]

    top3_data.append({
        "Country": country,
        "Top1": top3[0][0],
        "Top1_ratio": top3[0][1],
        "Top2": top3[1][0],
        "Top2_ratio": top3[1][1],
        "Top3": top3[2][0],
        "Top3_ratio": top3[2][1],
    })

    # Top1 카운트 집계
    top1_mbti = top3[0][0]
    top1_count[top1_mbti] = top1_count.get(top1_mbti, 0) + 1

# 정렬된 Top1 차트 데이터
chart_data = sorted(
    [{"MBTI": k, "Country Count": v} for k, v in top1_count.items()],
    key=lambda x: x["Country Count"],
    reverse=True
)

# MBTI 설명 사전
mbti_descriptions = {
    "INFJ": "🌱 이상주의자. 조용하고 통찰력 있으며 깊은 공감 능력 보유.",
    "INFP": "🎨 낭만주의자. 가치 중심적이며 감정이 풍부함.",
    "INTJ": "🧠 전략가. 논리적이며 장기적인 비전을 추구함.",
    "INTP": "🔬 분석가. 창의적이며 지적 호기심이 풍부함.",
    "ISFJ": "🛡️ 수호자. 조용하지만 헌신적인 성향.",
    "ISFP": "🎵 예술가. 자유롭고 감성적인 스타일.",
    "ISTJ": "📘 관리자. 실용적이고 책임감이 강함.",
    "ISTP": "🔧 장인. 논리적이며 도구와 기계에 익숙함.",
    "ENFJ": "🌟 주도자. 사람들과 잘 어울리고 리더십이 있음.",
    "ENFP": "🌈 활력소. 열정적이고 창의력이 넘침.",
    "ENTJ": "🪖 지휘관. 목표 지향적이며 조직화에 능함.",
    "ENTP": "💡 혁신가. 아이디어가 넘치고 논쟁을 즐김.",
    "ESFJ": "💞 사교가. 친절하고 타인을 돌보는 데 능함.",
    "ESFP": "🎉 연예인. 활발하고 사람을 즐겁게 함.",
    "ESTJ": "📋 감독관. 체계적이고 규칙에 강함.",
    "ESTP": "🏍️ 활동가. 모험을 즐기고 현실적인 해결책 선호."
}

# 제목
st.title("🧠 국가별 MBTI 유형 Top 3 분석")
st.markdown("각 국가에서 가장 비율이 높은 **상위 3개 MBTI 유형**을 분석하고 시각화합니다.")

# 차트
st.subheader("📊 가장 높은 비율로 나타난 MBTI Top1 유형 분포")

chart = alt.Chart(alt.Data(values=chart_data)).mark_bar().encode(
    x=alt.X("MBTI:N", sort="-y", title="MBTI 유형"),
    y=alt.Y("Country Count:Q", title="Top1으로 나타난 국가 수"),
    color=alt.Color("MBTI:N", legend=None),
    tooltip=["MBTI:N", "Country Count:Q"]
).properties(
    width=600,
    height=400,
    title="세계 각국에서 가장 비율이 높은 MBTI 유형"
)

st.altair_chart(chart, use_container_width=True)

# 선택 박스 및 풍선 효과
st.subheader("🔍 MBTI 유형별 설명 보기")
selected_mbti = st.selectbox("MBTI 유형을 선택하면 설명과 풍선 효과가 나옵니다!", mbti_types)

if selected_mbti:
    st.balloons()
    st.markdown(f"### ✨ {selected_mbti} 유형 설명")
    st.write(mbti_descriptions.get(selected_mbti, "설명이 준비되지 않았습니다."))

# 하단
st.markdown("---")
st.caption("데이터 출처: countriesMBTI_16types.csv | 시각화: Altair | 제작: Streamlit")
