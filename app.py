
import random
import streamlit as st

# 웹앱 제목
st.title("🍱 오늘의 점심 메뉴 추천")

# 메뉴 목록
menu_list = [
    "김치찌개",
    "제육볶음",
    "돈까스",
    "불고기",
    "비빔밥",
    "파스타",
    "햄버거",
    "초밥",
    "라면",
    "마라탕"
]

# 안내 문구
st.write("오늘 점심은 무엇을 먹을까요?")
st.write("아래 버튼을 눌러 메뉴를 추천받아 보세요!")

# 버튼 생성
if st.button("점심 메뉴 추천받기 🎲"):

    # 랜덤으로 메뉴 선택
    menu = random.choice(menu_list)

    # 결과 출력
    st.success(f"오늘의 점심 메뉴는 바로... {menu}입니다!")
