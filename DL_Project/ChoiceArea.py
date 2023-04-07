import streamlit as st

class GetSideBar:
    def __init__(self) -> None:
        self.sb = st.sidebar
        self.sb.error("## 지역을 선택해주세요.")
        
        self.area = ["", "경기도"]
        self.direction = [
            '', '가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', 
            '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주시', '연천군', 
            '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시'
            ]

        self.area_choice = self.sb.selectbox('지역 선택 그..치만....경기도 뿐인걸...', self.area)
        self.direction_choice = self.sb.selectbox('동서남북크로스', self.direction) if self.area_choice != "" else None
        self.address_input = self.sb.text_input("글램핑장명 입력") if self.area_choice and self.direction_choice != "" else None
    
    def choice_area(self) : return self.area_choice
    def choice_direction(self) : return self.direction_choice
    def input_address(self) : return self.address_input
    def result_sidebar(self) : return self.choice_area(), self.choice_direction(), self.input_address()