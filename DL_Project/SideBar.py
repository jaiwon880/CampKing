import streamlit as st
from Data import GetData

class GetSideBar:
    def __init__(self) -> None:
        self.sb = st.sidebar
        self.sb.write("## 🌳Go Glamping!🌳")
        self.df = GetData().create_data()

        self.area_choice = self.sb.selectbox('🌳Choice Area!🌳', self.get_area_list())
        self.direction_choice = self.sb.selectbox('🏕시, 군🏕', self.get_direction_list()) if self.area_choice != "" else None
        # self.address_choice = self.sb.selectbox('구, 동, 면, 군, 읍', self.get_address_list()) if self.area_choice and self.direction_choice != "" else None
    

    def split_location(self, index_num):
        return self.df.iloc[:, 3].apply(lambda x: x.split(' ')[index_num])

    def get_area_list(self) : 
        return [""] + list(set(self.split_location(0)))

    def get_direction_list(self) : 
        return [""] + sorted(list(set(self.df[self.split_location(0) == self.area_choice]\
                                                .iloc[:, 3].apply(lambda x: x.split(' ')[1]))))
    
    # def get_address_list(self) : 
    #     return [""] + sorted(list(set(self.df[(self.split_location(0) == self.area_choice)\
    #                                         & (self.split_location(1) == self.direction_choice)]\
    #                                             .iloc[:, 3].apply(lambda x: x.split(' ')[2]))))

    def set_choice_result_data(self):
        if self.area_choice != "" and self.direction_choice != "":
            return self.df[(self.split_location(0) == self.area_choice)\
                            & (self.split_location(1) == self.direction_choice)]
            # if self.address_choice != "" :
            #     return self.df[(self.split_location(0) == self.area_choice)\
            #                     & (self.split_location(1) == self.direction_choice)\
            #                     & (self.split_location(2) == self.address_choice)]
            # else :
            #     return self.df[(self.split_location(0) == self.area_choice)\
            #                     & (self.split_location(1) == self.direction_choice)]
        else : 
            return None

    def choice_result_sidebar(self) : 
        return self.set_choice_result_data(), self.area_choice, self.direction_choice