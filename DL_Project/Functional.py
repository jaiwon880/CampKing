from SideBar import GetSideBar
from Data import GetData

import streamlit as st
import random
import colorsys
import pandas as pd

import plotly.graph_objects as go
import matplotlib.pyplot as plotly

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
        if dic == "전체" : df = self.total
        elif dic == "가평군" : df = self.gapyeong
        elif dic == "포천시" : df = self.pocheon
        else : df = None

        saturation = 0.5
        lightness = 0.8

        colors = []
        for i in range(len(df)):
            r, g, b = [random.randint(150, 255) for j in range(3)]  # 밝은 색상을 위해 범위를 150~255로 조정
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            s = saturation
            v = lightness
            r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, s, v)]
            colors.append(f'rgb({r},{g},{b})')
        fig = go.Figure(go.Bar(y=df.index, x=df["🤜가격 산정"], orientation='h', marker=dict(color=colors)))
        
        fig.update_layout(
            title='😁 옵션 별 가격 순위표 😁', 
            title_font=dict(size=24),

            xaxis_title='가격', 
            xaxis_title_font_color='black',
            xaxis_title_font=dict(size=16),
            # yaxis_title='옵션',
            # yaxis_title_font_color='black',
            # yaxis_title_font=dict(size=14),

            xaxis=dict(tickfont=dict(color='green'), tickfont_size = 20),
            yaxis=dict(tickfont=dict(color='green'), tickfont_size = 20),
            
            width = 1400,
            height = 800,
            
            plot_bgcolor='rgb(230, 245, 230)',
            paper_bgcolor='#e6f5e6'
            )
        fig.update_xaxes(tickformat=",.0f")
        st.plotly_chart(fig)

        keyword = pd.DataFrame(df["🤜가격 산정"][:11]).transpose()
        st.dataframe(keyword)


    def choice_result(self) : return self.handle_df(self.df), self.area, self.direction

    def price_result(self): return self.handle_price(self.direction)

