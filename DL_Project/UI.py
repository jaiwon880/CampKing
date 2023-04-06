import streamlit as st
from Functional import GetResult
st.set_page_config(page_title="DL", layout="wide")
import folium
from streamlit_folium import folium_static

def test() : 
    return GetResult().result_function()

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


    # containers = [st.container() for i in range(len(image))]
    # for i in range(len(image)) :
    #     with containers[i] : 
    #         st.image(image[i], width = 700)
    # =========================================================
    # 서울 위도, 경도
    latitude = 37.5665
    longitude = 126.9780

    # 지도 생성
    map = folium.Map(location=[latitude, longitude], zoom_start=13)

    # streamlit에 지도 출력
    st.write(map._repr_html_(), unsafe_allow_html=True)

    # 서울 시청 위도, 경도
    city_hall_latitude = 37.5666791
    city_hall_longitude = 126.9782914

    # 마크 생성
    marker = folium.Marker(location=[city_hall_latitude, city_hall_longitude], popup='서울 시청')

    # 마크를 지도에 추가
    marker.add_to(map)

    # streamlit에 지도 출력
    st.write(map._repr_html_(), unsafe_allow_html=True)