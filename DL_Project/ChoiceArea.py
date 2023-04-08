import streamlit as st
from Data import GetData

class GetSideBar:
    def __init__(self) -> None:
        self.sb = st.sidebar
        self.sb.error("## 지역을 선택해주세요.")

        self.df = GetData().create_data()
        
        self.area = [""] + self.df["경기도"].unique().tolist()
        # self.direction = [
        #     '', '가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', 
        #     '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주시', '연천군', 
        #     '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시'
        #     ]
        self.area_choice = self.sb.selectbox('지역 선택 그..치만....경기도 뿐인걸...', self.area)

        self.direction = [""] + self.df[self.df[self.area_choice] == self.area_choice].drop_duplicates(subset='시, 군')['시, 군'].tolist()
        self.direction_choice = self.sb.selectbox('동서남북크로스', self.direction) if self.area_choice != "" else None
        self.address_input = self.sb.text_input("글램핑장명 입력(동, 면이 될 수도)") if self.area_choice and self.direction_choice != "" else None

    def result_sidebar(self) : return self.area_choice, self.direction_choice, self.address_input