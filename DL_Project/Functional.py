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

# class Map:
#     def __init__(self) -> None:
#         # 서울 위도, 경도
#         self.latitude = 37.5665
#         self.longitude = 126.9780

#         # 서울 시청 위도, 경도
#         self.city_hall_latitude = 37.5666791
#         self.city_hall_longitude = 126.9782914

#         # 지도 생성
#         self.map = folium.Map(location=[self.latitude, self.longitude], zoom_start=13)
#         # 마크 생성
#         self.marker = folium.Marker(location=[self.city_hall_latitude, self.city_hall_longitude], popup='서울 시청')

#     # streamlit에 지도 출력
#     def create_map(self):
#         self.map._reper_html_(), unsafe_allow_html=True
#         self.marker.add_to(self.map)
#         return self.map
    
#     def result_map(self):
#         return self.create_map()