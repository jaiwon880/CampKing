import streamlit as st
import pandas as pd
from Functional import GetResult

st.set_page_config(page_title="DL", layout="wide")

def get() : return GetResult().get_result()

def user_interface():
    st.error("## TDD - Testing...")
    df, area, direction, address = get()

    # 사이드바 
    with st.sidebar :
        if df is not None : st.dataframe(df, width = 300)
       
    st.write(f"""
            ### 지역 선택 = {area}
            ### 지역 선택 후 지역들 = {direction}
            ### 유저 인풋 데이터 = {address}
            ### 데이터프레임👇
    """)

    st.write(f"""
            {df}
    """)

    # image = [
    #     "https://i.imgur.com/t4O7ozH.jpg", 
    #     "https://i.imgur.com/idnsDBs.gif", 
    #     "https://i.imgur.com/fvRG1Tj.gif"
    #     ]

    # for i in range(len(image)) :
    #     with st.expander(f"사진_{i+1}"):
    #         st.image(image[i])


    # containers = [st.container() for i in range(len(image))]
    # for i in range(len(image)) :
    #     with containers[i] : 
    #         st.image(image[i], width = 700)
    # # =====================================================================
    # messages = ['success', 'info', 'warning', 'error']

    # for i in range(2):
    #     for message in messages:
    #         getattr(st, message)(f'This is a {message} message')