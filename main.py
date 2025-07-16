import streamlit as st

# 웹페이지 기본 설정
st.set_page_config(page_title="MBTI별 포켓몬 추천", page_icon="✨", layout="centered")

# 앱 제목
st.title("🌟 MBTI별 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬 캐릭터를 추천해드릴게요!")

# MBTI 목록
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 포켓몬 추천 정보
pokemon_data = {
    "ISTJ": {"name": "리자몽", "desc": "🔥 책임감 강한 당신에겐 듬직한 리자몽!", "img": "charizard"},
    "ISFJ": {"name": "이브이", "desc": "🧡 배려심 깊은 당신에겐 변화무쌍한 이브이!", "img": "eevee"},
    "INFJ": {"name": "뮤", "desc": "✨ 신비로운 당신에겐 전설의 뮤!", "img": "mew"},
    "INTJ": {"name": "뮤츠", "desc": "🧠 전략가형 당신에겐 지능적인 뮤츠!", "img": "mewtwo"},
    "ISTP": {"name": "팬텀", "desc": "🕶️ 조용한 행동파, 그림자처럼 움직이는 팬텀!", "img": "gengar"},
    "ISFP": {"name": "피카츄", "desc": "⚡ 따뜻하고 조용한 당신에겐 사랑스러운 피카츄!", "img": "pikachu"},
    "INFP": {"name": "루기아", "desc": "🌊 감성 충만한 당신에겐 평화를 상징하는 루기아!", "img": "lugia"},
    "INTP": {"name": "프테라", "desc": "🦖 호기심 많은 당신에겐 고대의 지성 프테라!", "img": "aerodactyl"},
    "ESTP": {"name": "갸라도스", "desc": "💥 역동적인 당신에겐 폭발력 있는 갸라도스!", "img": "gyarados"},
    "ESFP": {"name": "푸린", "desc": "🎤 모두의 스타인 당신에겐 귀염둥이 푸린!", "img": "jigglypuff"},
    "ENFP": {"name": "에브이", "desc": "🌈 열정적이고 상상력 풍부한 당신에겐 에브이!", "img": "espeon"},
    "ENTP": {"name": "디그다", "desc": "😆 재치 있는 당신에겐 어디서든 튀어나오는 디그다!", "img": "diglett"},
    "ESTJ": {"name": "거북왕", "desc": "🛡️ 체계적이고 강직한 당신에겐 믿음직한 거북왕!", "img": "blastoise"},
    "ESFJ": {"name": "푸크린", "desc": "🎀 다정한 당신에겐 포근한 푸크린!", "img": "wigglytuff"},
    "ENFJ": {"name": "라프라스", "desc": "🛳️ 이끄는 리더! 따뜻한 라프라스!", "img": "lapras"},
    "ENTJ": {"name": "마기라스", "desc": "👑 카리스마의 끝판왕! 당신은 마기라스!", "img": "tyranitar"},
}

# MBTI 선택
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요", mbti_types)

# 결과 출력
if selected_mbti:
    result = pokemon_data[selected_mbti]
    st.markdown("---")
    st.subheader(f"🎉 추천 포켓몬: {result['name']}")
    st.write(result["desc"])
    
    # 이미지 출력 (PokémonDB 이미지 URL 사용)
    image_url = f"https://img.pokemondb.net/artwork/large/{result['img']}.jpg"
    st.image(image_url, caption=result["name"], use_column_width=True)

# 하단 문구
st.markdown("---")
st.caption("✨ 포켓몬 이미지는 pokemondb.net에서 제공됩니다 | Made with ❤️ by Streamlit")
