import streamlit as st
from Functional import GetResult
st.set_page_config(page_title="DL", layout="wide")

import folium

def test() : 
    return GetResult().result_function()

def user_interface():
    # folium 지도 객체 생성
    m = folium.Map(location=[37.566345, 126.977893], zoom_start=13)

    # streamlit 컴포넌트에 folium 지도 렌더링
    st.write(m._repr_html_(), unsafe_allow_html=True)

    # 마커 추가
    folium.Marker(location=[37.566345, 126.977893], popup='서울특별시청').add_to(m)

    # 선 추가
    locations = [[37.566345, 126.977893], [37.5658859, 126.9754788]]
    folium.PolyLine(locations=locations, color='red').add_to(m)

    # streamlit 컴포넌트에 folium 지도 렌더링
    st.write(m._repr_html_(), unsafe_allow_html=True)

    # st.title("뼈대 작업 중...")
    # result1, result2 = test()
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