import streamlit as st
from Functional import GetResult
st.set_page_config(page_title="DL", layout="wide")

def test() : return GetResult().result_function()

def user_interface():
    st.error("## TDD - Testing...")
    result1, result2, result3, result4 = test()

    with st.sidebar :
        # 사이드바 
        if result1 is not None : st.dataframe(result1)
        else : pass 
    
    
    st.write(f"""
    ### TDD중
    ### 여백 경기도 선택칸 {result2}
    ### 경기도 선택칸 {result3}
    ### 업체명 검색칸 {result4}
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
    # =====================================================================
    messages = ['success', 'info', 'warning', 'error']

    for i in range(2):
        for message in messages:
            getattr(st, message)(f'This is a {message} message')