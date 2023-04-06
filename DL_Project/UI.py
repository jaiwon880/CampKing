import streamlit as st
from Functional import GetResult
st.set_page_config(page_title="DL", layout="wide")

def test() : return GetResult().result_function()

def user_interface():
    st.title("뼈대 작업 중...")
    result1, result2 = test()
    result2 = True if result2 is None else False

    st.write(f"""
        ### ChoiceArea -> Functional ->  UI 모듈 연동 결과는? = {result1}
        ### Data -> Functional -> UI 모듈 연동 결과는? = {result2}
    """)

    image = [
        "https://i.imgur.com/t4O7ozH.jpg", 
        "https://i.imgur.com/idnsDBs.gif", 
        "https://i.imgur.com/fvRG1Tj.gif"
        ]

    for i in range(len(image)) :
        with st.expander(f"사진_{i+1}"):
            st.image(image[i])


    containers = [st.container() for i in range(len(image))]
    for i in range(len(image)) :
        with containers[i] : 
            st.image(image[i], width = 700)
    # =========================================================