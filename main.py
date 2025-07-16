import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="🎈",
    layout="centered"
)

# 타이틀
st.title("🎈 MBTI로 알아보는 나와 어울리는 포켓몬!")
st.markdown("MBTI를 선택하면, 당신의 성격과 잘 어울리는 포켓몬을 귀여운 이미지와 함께 추천해드려요 😊")

# MBTI 리스트
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 포켓몬 추천 데이터
pokemon_dict = {
    "ISTJ": {
        "name": "리자몽",
        "desc": "🔥 신중하고 책임감 있는 당신은, 강인하면서도 믿음직한 리자몽과 닮았어요.\n열정이 속에 숨겨진 타입! 타인을 위해 기꺼이 싸우는 전사 스타일!",
        "img": "charizard"
    },
    "ISFJ": {
        "name": "이브이",
        "desc": "🧡 배려 깊고 포용력 있는 당신에겐 다양한 모습으로 진화할 수 있는 이브이가 딱!\n주변 사람을 편안하게 해주는 힐러 타입이에요.",
        "img": "eevee"
    },
    "INFJ": {
        "name": "뮤",
        "desc": "✨ 이상주의적이고 신비로운 당신은, 전설의 포켓몬 뮤와 어울려요.\n창의적이고 세상을 더 나은 곳으로 만들고 싶은 마음이 가득하죠.",
        "img": "mew"
    },
    "INTJ": {
        "name": "뮤츠",
        "desc": "🧠 계획적이고 전략적인 당신에겐 강력한 지능형 포켓몬, 뮤츠가 어울려요.\n냉철하지만 따뜻한 내면을 지닌 리더형 타입입니다.",
        "img": "mewtwo"
    },
    "ISTP": {
        "name": "팬텀",
        "desc": "🕶️ 침착하고 유연한 성격의 당신에겐 그림자처럼 자유롭게 움직이는 팬텀이 어울려요.\n위기 대처 능력이 뛰어난 생존형 캐릭터!",
        "img": "gengar"
    },
    "ISFP": {
        "name": "피카츄",
        "desc": "⚡ 감성적이고 따뜻한 당신에겐 모두가 사랑하는 피카츄가 찰떡이에요.\n겉보기엔 소심하지만, 친구를 위해 강해지는 헌신형!",
        "img": "pikachu"
    },
    "INFP": {
        "name": "루기아",
        "desc": "🌊 조용하고 깊은 성찰을 지닌 당신에겐 바다를 품은 루기아가 어울려요.\n감성적이고 평화를 사랑하는 이상주의자입니다.",
        "img": "lugia"
    },
    "INTP": {
        "name": "프테라",
        "desc": "🦖 논리적이고 분석적인 당신에겐 고대의 지혜를 간직한 프테라가 제격이에요.\n지식과 호기심으로 세상을 탐험하는 탐구자형!",
        "img": "aerodactyl"
    },
    "ESTP": {
        "name": "갸라도스",
        "desc": "💥 에너지 넘치고 도전적인 당신에겐 폭풍 같은 갸라도스가 어울려요.\n상황에 민첩하게 대응하며, 위기를 기회로 바꾸는 전투형!",
        "img": "gyarados"
    },
    "ESFP": {
        "name": "푸린",
        "desc": "🎤 밝고 사교적인 당신에겐 사랑스러운 매력의 푸린이 잘 어울려요.\n분위기 메이커로 모두를 웃게 만드는 긍정 에너지!",
        "img": "jigglypuff"
    },
    "ENFP": {
        "name": "에브이",
        "desc": "🌈 열정적이고 창의적인 당신에겐 마법 같은 에브이가 제격이에요.\n자유로운 상상력과 친화력으로 모두와 잘 지내는 만능형!",
        "img": "espeon"
    },
    "ENTP": {
        "name": "디그다",
        "desc": "😆 재치 있고 호기심 많은 당신에겐 어디서든 등장하는 디그다가 딱이에요.\n빠른 순발력과 재치로 대화를 이끄는 아이디어 뱅크!",
        "img": "diglett"
    },
    "ESTJ": {
        "name": "거북왕",
        "desc": "🛡️ 책임감 있고 체계적인 당신에겐 튼튼하고 신뢰감 있는 거북왕이 어울려요.\n정의롭고 믿음직한 현실 리더형 캐릭터!",
        "img": "blastoise"
    },
    "ESFJ": {
        "name": "푸크린",
        "desc": "🎀 따뜻하고 온화한 당신에겐 포근한 푸크린이 잘 어울려요.\n타인을 잘 돌보고 배려하며, 모두가 의지하는 존재!",
        "img": "wigglytuff"
    },
    "ENFJ": {
        "name": "라프라스",
        "desc": "🛳️ 공감 능력 뛰어난 당신에겐 모두를 태워주는 라프라스가 어울려요.\n함께하는 이들에게 따뜻한 힘이 되는 리더형 포켓몬!",
        "img": "lapras"
    },
    "ENTJ": {
        "name": "마기라스",
        "desc": "👑 강한 추진력과 카리스마의 당신에겐 절대 보스, 마기라스!\n목표를 향해 직진하며 주변을 압도하는 리더십!",
        "img": "tyranitar"
    }
}

# 사용자 선택
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요", mbti_list)

# 결과 출력
if selected_mbti:
    poke = pokemon_dict[selected_mbti]
    
    st.balloons()  # 🎈 풍선 효과!
    
    st.markdown("---")
    st.subheader(f"🎉 당신에게 어울리는 포켓몬은 바로... **{poke['name']}**!")
    st.write(poke["desc"])

    image_url = f"https://img.pokemondb.net/artwork/large/{poke['img']}.jpg"
    st.image(image_url, caption=poke["name"], use_container_width=True)

# 하단 안내
st.markdown("---")
st.caption("🧡 이 앱은 Streamlit으로 만들어졌으며, 포켓몬 이미지는 pokemondb.net에서 제공됩니다.")
