import streamlit as st
from Functional import GetResult
st.set_page_config(page_title="DL", layout="wide")

import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

def test() : 
    return GetResult().result_function()

def user_interface():
    st.title("뼈대 작업 중...")
    result1, result2 = test()
    # result2 = True if result2 is None else False

    # st.write(f"""
    #     ### ChoiceArea -> Functional ->  UI 모듈 연동 결과는? = {result1}
    #     ### Data -> Functional -> UI 모듈 연동 결과는? = {result2}
    # """)

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
    # =========================================================
    st.set_page_config(page_title="Map Example")

    st.components.v1.html(open("map.html", "r").read(), width=700, height=500)

    # 서울 시청의 위도, 경도
    seoul_city_hall = [37.5665, 126.978]

    # folium으로 지도 생성
    m = folium.Map(location=seoul_city_hall, zoom_start=12)

    # streamlit에 지도 표시
    st.markdown(m._repr_html_(), unsafe_allow_html=True)

    