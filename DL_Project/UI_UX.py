import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plotly
import random
import math
import colorsys
import base64
from pydub.playback import play
from Functional import GetResult


def set_page() : st.set_page_config(page_title="for Doksan Seo teacher",
                                    page_icon="🏕️", 
                                    layout="wide", 
                                    initial_sidebar_state="auto",)




class User_Interface :
    def __init__(self) -> None:
        self.get = GetResult()

        self.df, \
        self.area, \
        self.direction = self.get.choice_result()

        self.price_df = self.get.price_result()
        
        self.ment = "수술 중😑"
        self.split_count = 10 # 프레임 자르는 개수 기준 
        self.left_column, self.right_column = st.columns([3, 7])

    def choice_result(self) : return self.df, self.direction

    def set_column(self) : return self.left_column, self.right_column

    def cutting(self): return st.markdown("---")

    def set_background(self) : st.markdown("""<style>
                                            .main {
                                                background-image: url('https://t1.daumcdn.net/cfile/blog/99C6924C5B65B8BD02');
                                                background-size: cover;
                                                }
                                            </style> """, unsafe_allow_html=True)
        
    def start_background(self): st.markdown("""<style>
                                            .main {
                                                background-image: url('https://i.imgur.com/idnsDBs.gif');
                                                background-size: cover;
                                                }
                                            </style> """, unsafe_allow_html=True)

    def result_ment(self) : st.markdown(f"<div style='background-color: green; \
                                            padding: 10px; color: white; font-size: 48px;\
                                            font-weight: bold; display: inline-block;'> \
                                            👉{self.area} {self.direction} {len(self.df)}개 의 업체 분석 결과\
                                            </div>", unsafe_allow_html=True) 

    def refactoring_ment(self) : st.markdown(f"<div style='background-color: white; \
                                                padding: 10px; color: green; font-size: 48px;\
                                                font-weight: bold; display: inline-block;'> \
                                                👉{self.ment} \
                                                </div>", unsafe_allow_html=True)
    def sidebar_print_df(self):
        if len(self.df) > 10 :
            st.write("# Best!"), st.dataframe(self.df.head(), width=600)
            st.write("# Worst!"), st.dataframe(self.df.tail(), width=600)
        else : st.write("분석할 업체의 수 가 충분하지 않습니다.")  
         
    def print_graph(self) :
        saturation = 0.5
        lightness = 0.8

        colors = []
        for i in range(len(self.price_df)):
            r, g, b = [random.randint(150, 255) for j in range(3)]  # 밝은 색상을 위해 범위를 150~255로 조정
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            s = saturation
            v = lightness
            r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, s, v)]
            colors.append(f'rgb({r},{g},{b})')
        fig = go.Figure(go.Bar(y=self.price_df.index, x=self.price_df["🤜가격 산정"], orientation='h', marker=dict(color=colors)))
        
        fig.update_layout(
            title='😁 옵션 별 가격 순위표 😁', 
            title_font=dict(size=24),

            xaxis_title='가격', 
            xaxis_title_font_color='green',
            xaxis_title_font=dict(size=16),
            # yaxis_title='옵션',
            # yaxis_title_font_color='black',
            # yaxis_title_font=dict(size=14),

            xaxis=dict(tickfont=dict(color='green'), tickfont_size = 20),
            yaxis=dict(tickfont=dict(color='green'), tickfont_size = 20),
            
            width = 1000,
            height = 1400,
            
            plot_bgcolor='rgb(230, 245, 230)',
            paper_bgcolor='#e6f5e6'
            )
        fig.update_xaxes(tickformat=",.0f")

        st.plotly_chart(fig)

    def print_price(self) :
        # for i in range(math.ceil(len(self.price_df) / self.split_count)):
        #     start_idx = i * self.split_count
        #     end_idx = min(start_idx + self.split_count, len(self.price_df))

        #     dfs = []
        #     for col in self.price_df.columns:
        #         dfs.append(self.price_df[col][start_idx:end_idx].round(0).astype(int))
            
        #     # 수평으로 병합하기
        #     merged_df = pd.concat(dfs, axis=1)
            
        #     # 줄바꿈 무시하고 출력하기
        #     st.dataframe(merged_df.to_string(index=True, header=False, col_space=12, line_width=100000), unsafe_allow_html=True)
            # st.write(keywor_price.T.style.set_table_styles([{'selector': 'th', 'props': [('max-width', '50px')]}]), width=1200)
            # st.dataframe(keywor_price, width = 1200)
        # ========================================================================================================================
        # for i in range(math.ceil(len(self.price_df)/self.split_count)):
        #     start_idx = i * self.split_count
        #     end_idx = min(start_idx+self.split_count, len(self.price_df))
            
        #     keywor_price = pd.DataFrame(self.price_df["🤜가격 산정"][start_idx:end_idx]).transpose().round(0).astype(int)
        #     st.dataframe(keywor_price, width = 1200)
        # ========================================================================================================================
        for i in range(0, len(self.price_df), self.split_count):
            keywor_price = self.price_df.iloc[i:i+self.split_count]["🤜가격 산정"].astype(int).round(0).transpose()
            st.dataframe(keywor_price, 500)

class User_Experience :
    def __init__(self) -> None:
        self.audio_path = "DL_Project/Data_csv/outdoor_crackling_fire_sound.mp3"
        self.audio = open(self.audio_path, 'rb').read()

    def set_BGM(self) : st.markdown(f'<audio autoplay loop="true" src="data:audio/mp3;base64,\
                                        {base64.b64encode(self.audio).decode()}"></audio>',\
                                        unsafe_allow_html = True)