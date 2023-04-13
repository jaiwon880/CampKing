from SideBar import GetSideBar
from Data import GetData

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

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
            df = df.drop_duplicates(subset=['name'], keep='first')
            df.sort_values(by='ranking', ascending=False, inplace=True)
            df = df[['name', 'ranking']].reset_index(drop=True)
            df.index.name = "🏆 순위"
            df = df.rename(columns={'name': '🏕️ 업체명', 'ranking': '⭐ 별점'})
            df.index += 1
            return df
            
        else : return None

    def choice_result_df(self) : 
        return self.handle_df(self.df) if self.df is not None else None

    def get_result(self) : 
        return self.choice_result_df(), self.area, self.direction

    def total_price(self):
        total_ranking_keyword = pd.DataFrame(self.total["importance"][:11]).transpose()

        fig, ax = plt.subplots(figsize=(10, 8))
        self.total.plot(kind="barh", ax=ax)

        st.image("https://i.imgur.com/qZJvwRB.png")
        st.pyplot(fig)
        st.write(total_ranking_keyword)
    
    def gapyeong_price(self):
        gapyeong_ranking_keyword = pd.DataFrame(self.gapyeong['importance'][:11]).transpose()

        fig, ax = plt.subplots(figsize=(10, 8))
        self.gapyeong.plot(kind='barh', ax=ax)

        st.image("https://i.imgur.com/Bgv83pb.png")
        st.pyplot(fig)
        st.write(gapyeong_ranking_keyword)

    def pocheon_load():
        pocheon_ranking_keyword = pd.DataFrame(self.pocheon['importance'][:11]).transpose()

        fig, ax = plt.subplots(figsize=(10, 8))
        pocheon.plot(kind='barh', ax=ax)

        st.image("https://i.imgur.com/QGxbZJa.png")
        st.pyplot(fig)
        st.write(pocheon_ranking_keyword)