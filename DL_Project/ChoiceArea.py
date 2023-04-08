import streamlit as st
from Data import GetData

class GetSideBar:
    def __init__(self) -> None:
        self.sb = st.sidebar
        self.sb.write("## 지역을 선택해주세요.")

        self.df = self.get_data()
        
        self.area_choice = self.sb.selectbox('팔도비빔면 그..치만....경기도 뿐인걸...', self.get_area_list())
        self.direction_choice = self.sb.selectbox('네넴띤선택결과', self.get_direction_list()) if self.area_choice != "" else None
        self.address_input = self.sb.text_input("글램핑장명으로 구현 중 후에(동, 면 수정)") if self.area_choice and self.direction_choice != "" else None
    
    def get_area_list(self) : return [""] + self.df.iloc[:, 0].drop_duplicates().tolist()
    def get_direction_list(self) : return [""] + self.df[self.df[self.df.columns[0]] == self.area_choice]\
                                                .drop_duplicates(subset=self.df.columns[1])[self.df.columns[1]]\
                                                .sort_values().tolist() if self.area_choice != "" else None

    def get_data(self) : return GetData().create_data()
    def set_data(self) : return self.df[(self.df[self.df.columns[0]] == self.area_choice)\
                                         & (self.df[self.df.columns[1]] == self.direction_choice)]\
                                         if self.area_choice and self.direction_choice != "" else None

    def get_choice_result(self) : return self.area_choice, self.direction_choice, self.address_input


















    # self.direction = [
        #     '', '가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', 
        #     '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주시', '연천군', 
        #     '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시'
        #     ]
    # self.direction = [""] + self.df[self.df[self.area_choice] == self.area_choice].drop_duplicates(subset='시, 군')['시, 군'].tolist() if self.area_choice != "" else None