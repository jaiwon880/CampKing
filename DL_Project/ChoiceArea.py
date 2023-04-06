import streamlit as st

class GetSideBar:
    def __init__(self) -> None:
        self.sb = st.sidebar
        self.sb.title('지역을 선택해주세요.')
        
        self.area = ["", "경기도"]
        self.direction = ["", "경기 동부", "경기 서부", "경기 남부", "경기 북부"]

        self.area_choice = self.sb.selectbox('지역 선택 그..치만....경기도 뿐인걸...', self.area)
        
        self.direction_choice = self.sb.selectbox('동서남북크로스', self.direction) if self.area_choice != "" else None

        self.district_choice = self.sb.selectbox('동네 입력해주세요', self.direction) if self.direction_choice != "" and not None else None

    def choice_sidebar(self) : 
        return self.district_choice
        
    def result_sidebar(self) : 
        return self.choice_sidebar()