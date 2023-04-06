import folium
from ChoiceArea import GetSideBar
from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().result_data()
        self.choice = self.backend_function()

    def backend_function(self) : 
        return GetSideBar().result_sidebar()

    def result_function(self) : 
        return self.choice, self.df

class Map:
    def __init__(self) -> None:
        pass
    # # 서울 위도, 경도
    # latitude = 37.5665
    # longitude = 126.9780

    # # 지도 생성
    # map = folium.Map(location=[latitude, longitude], zoom_start=13)

    # # streamlit에 지도 출력
    # st.write(map._repr_html_(), unsafe_allow_html=True)

    # # 서울 시청 위도, 경도
    # city_hall_latitude = 37.5666791
    # city_hall_longitude = 126.9782914

    # # 마크 생성
    # marker = folium.Marker(location=[city_hall_latitude, city_hall_longitude], popup='서울 시청')

    # # 마크를 지도에 추가
    # marker.add_to(map)

    # # streamlit에 지도 출력
    # st.write(map._repr_html_(), unsafe_allow_html=True)