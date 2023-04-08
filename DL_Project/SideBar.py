import streamlit as st
from Data import GetData

class GetSideBar:
    def __init__(self) -> None:
        self.sb = st.sidebar
        self.sb.write("## 지역을 선택해주세요.")
        self.df = GetData().create_data()

        self.area_choice = self.sb.selectbox('팔도비빔면 그..치만....경기도 뿐인걸...', self.get_area_list())
        self.direction_choice = self.sb.selectbox('네넴띤선택결과', self.get_direction_list()) if self.area_choice != "" else None
        self.address_input = self.sb.text_input("글램핑장명으로 구현 중 후에(동, 면 수정)") if self.area_choice and self.direction_choice != "" else None
    
    def get_area_list(self):
        return [""] + self.df.iloc[:, 0].drop_duplicates().tolist()

    def get_direction_list(self):
        if self.area_choice != "":
            return [""] + self.df[self.df[self.df.columns[0]] == self.area_choice] \
                                .drop_duplicates(subset=self.df.columns[1])[self.df.columns[1]] \
                                .sort_values().tolist()
        else : return None
    
    def set_data(self):
        if self.area_choice != "" and self.direction_choice != "":
            if self.address_input != "" :
                return self.df[(self.df[self.df.columns[0]] == self.area_choice)
                            & (self.df[self.df.columns[1]] == self.direction_choice)
                            & (self.df[self.df.columns[2]].str.contains(self.address_input))]
            else:
                return self.df[(self.df[self.df.columns[0]] == self.area_choice)
                            & (self.df[self.df.columns[1]] == self.direction_choice)]
        else : return None


    def get_choice_result(self):
        return self.area_choice, self.direction_choice, self.address_input