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
        
        self.image_path = ["https://i.imgur.com/qZJvwRB.png", \
                            "https://i.imgur.com/Bgv83pb.png", \
                            "https://i.imgur.com/QGxbZJa.png"]
    def get_result(self) : 
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
        df, image_path = self.handle_price()
        df = self.rename_df(df)

        if df is not None and image_path is not None:
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
            fig.update_xaxes(tickformat=".0f")
            
            st.image(image_path)
            st.plotly_chart(fig)
            st.dataframe(keyword)
        else:
            pass

    def handle_price(self) : 
        if self.direction == "전체" : return self.total, self.image_path[0]
        elif self.direction == "가평군" : return self.gapyeong, self.image_path[1]
        elif self.direction == "포천시" : return self.pocheon, self.image_path[2]
        else : return None, None

    def rename_df(self, df) : 
        df = df.rename(columns={"importance" : "🤜가격 산정"})
        df = df.rename(index={\
        "info_bogcheung": "복층식🏠",\
        'name': '이름(인지도)🌞',\
        'ranking': '리뷰 별점⭐',\
        'info_glamping': '글램핑🏕️',\
        'info_poolvilla': '풀빌라 수영장🏊',\
        'roomname': '숙박🛏️',\
        'info_caravan': '카라반🚐',\
        'max_standard': '최대 인원수👥',\
        'info_privatehouse': '전원주택🏡',\
        'visitor_photo': '사진 촬영📷',\
        'visitor_entertainment': '주변 관광지🏞️',\
        'info_pension': '펜션🏘️',\
        'info_bathroom': '개별 욕실🛁',\
        'visitor_clean': '청결도🧼',\
        'info_spa': '스파/월풀/사우나/마사지💆‍♂️',\
        'visitor_view': '전망🌅',\
        'info_deck': '테라스/데크🪑',\
        'info_terrace': '테라스🌳',\
        'people_stadard': '표준 인원수👥',\
        'visitor_bbq': '바베큐시설🍖',\
        'visitor_sink': '세탁기/식기세척기🧺',\
        'info_grass': '잔디밭/초원🌿',\
        'info_oceanview': '오션뷰/해운대뷰🌊',\
        'visitor_maintainance': '유지보수🛠️',\
        'visitor_kind': '친절도🙂',\
        'visitor_rest': '휴식공간🧘‍♀️',\
        'visitor_goodprice': '가성비👍',\
        'info_unisex': '남녀공용화장실🚻',\
        'visitor_parking': '주차시설🅿️',\
        'visitor_publictransport': '대중교통🚉',\
        'visitor_hotwater': '온수/정수기🚰',\
        'visitor_waterplay': '수영장/물놀이시설🏊',\
        'visitor_mannertime': '체크인/아웃 시간⏰',\
        'visitor_bathroom': '욕실청소상태🚽',\
        'visitor_interior': '인테리어/가구🛋️',\
        'info_ondolroom': '온돌/한옥🏯',\
        'homepage': '홈페이지🌐',\
        'visitor_shade': '그늘막/텐트/파라솔☂️',\
        'visitor_wide': '넓이/공간📏',\
        'visitor_concept': '컨셉🎨',\
        'visitor_child': '어린이 놀이시설',\
        'homepage': '홈페이지🌐',\
        'visitor_shade': '그늘막/텐트/파라솔☂️',\
        'visitor_wide': '넓이/공간📏',\
        'visitor_concept': '컨셉🎨',\
        'visitor_child': '어린이 놀이시설🤸‍♀️',\
        'visitor_temperature': '온도/냉방/난방❄️',\
        'visitor_facility': '시설🚪',\
        'visitor_noise': '소음🔇',\
        'visitor_bed': '침대/이불🛏️',\
        'visitor_pet': '애완동물🐶',\
        "info_menonly": "남성 전용🧔‍♂️",\
        "info_partyroom": "파티룸🎉",\
        "info_womenonly": "여성 전용👩‍🦰",\
        "visitor_worthy": "방문 가치💯",\
        "visitor_party": "파티하기 좋아요🥳",\
        "visitor_bug": "벌레 조심🐛"
        })
        
        return df