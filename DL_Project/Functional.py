from SideBar import GetSideBar
from Data import GetData

import random
import streamlit as st
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
        
    def get_choice_result(self) : 
        return self.choice_result_df(), self.area, self.direction

    def choice_result_df(self) : 
        return self.handle_df(self.df) if self.df is not None else None

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

    def get_price(self):
        # df = self.rename_df(self.handle_price())
        df = self.handle_price()

        if df is not None :
            keyword = pd.DataFrame(df["🤜가격 산정"][:11]).transpose()
            colors = ['rgb({},{},{})'.format(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for i in range(len(df))]
            fig = go.Figure(go.Bar(y=df.index, x=df["🤜가격 산정"], orientation='h', marker=dict(color=colors)))
            
            fig.update_layout(
                title='😁 옵션 별 가격 순위표 😁', 
                xaxis_title='가격', 
                yaxis_title='옵션',
                width = 1200,
                height = 800,
                plot_bgcolor='rgb(255, 255, 204)',
                # paper_bgcolor='rgb(255, 255, 204)'
                )
            # fig.update_xaxes(tickformat=",.0f", tickprefix="$")
            fig.update_xaxes(tickformat=" ,.0f", ticktext=[f"{val:,}원" for val in fig.data[0].x])

            # st.image(image_path)
            st.plotly_chart(fig)
            st.dataframe(keyword)
        else:
            pass

    def handle_price(self) : 
        if self.direction == "전체" : return self.total
        elif self.direction == "가평군" : return self.gapyeong
        elif self.direction == "포천시" : return self.pocheon
        else : return None