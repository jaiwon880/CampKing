from SideBar import GetSideBar
from Data import GetData

import streamlit as st





class GetResult:
    def __init__(self) -> None:
        self.df, \
        self.area, \
        self.direction = GetSideBar().choice_result_sidebar()

        self.total, \
        self.gapyeong, \
        self.pocheon = GetData().create_price()

    def handle_df(self, df) :
        if df is not None :
            df = (df.drop_duplicates(subset=['name'], keep='first')\
                    .sort_values(by='ranking', ascending=False)\
                    [['name', 'ranking']]\
                    .rename(columns={'name': '🏕️ 업체명', 'ranking': '⭐ 별점'})\
                    .reset_index(drop=True))
            df.index.name = "🏆 순위"
            df.index += 1
            return df
            
        else : return None

    def handle_price(self, dic) : 
        if dic == "전체" : return self.total
        elif dic == "가평군" : return self.gapyeong
        elif dic == "포천시" : return self.pocheon
        else : return

    def choice_result(self) : return self.handle_df(self.df), self.area, self.direction

    def price_result(self) : 
        return self.handle_price(self.direction)