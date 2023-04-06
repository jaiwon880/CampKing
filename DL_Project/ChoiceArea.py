import streamlit as st
from Data import GetData

class GetSideBar:
    def __init__(self) -> None:
        self.sb = st.sidebar
        self.sb.title('지역을 선택해주세요.')

        self.df = GetData().result_data()
        self.result_df = None
        
        self.area = ["경기도"]
        self.direction = ["경기 동부", "경기 서부", "경기 남부", "경기 북부"]

        self.area_choice = self.sb.selectbox('지역 선택 그..치만....경기도 뿐인걸...', self.area)
        self.direction_choice = self.sb.selectbox('동서남북크로스', self.direction)

    def functional_sidebar(self) : 
        # 기능부 연동 작성 예정 
        self.result_df = self.direction_choice 
        return self.result_df

    def result_sidebar(self) :
        return self.functional_sidebar()