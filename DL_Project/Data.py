import pandas as pd
import streamlit as st
import pickle

# @st.cache
class GetData:
    def __init__(self) -> None : 
        self.path = ["DL_Project/Data_csv/df_final.csv",\
                    "DL_Project/Data_csv/total.csv",\
                    "DL_Project/Data_csv/gapyeong.csv",\
                    "DL_Project/Data_csv/pocheon.csv"]

        self.df = self.load_data()
        self.total, \
        self.gapyeong, \
        self.pocheon = self.load_price()

    def load_data(self):
        try :  
            return pd.read_csv(self.path[0])
        except Exception as e : 
            return st.error(e)

    def load_price(self) :
        try:
            return self.rename_df(pd.read_csv(self.path[1], index_col =0, encoding="utf-8")),\
                    self.rename_df(pd.read_csv(self.path[2], index_col =0, encoding="utf-8")),\
                    self.rename_df(pd.read_csv(self.path[3], index_col =0, encoding="utf-8"))

        except Exception as e:
            return st.error(e)

    def create_data(self) : 
        return self.df

    def create_price(self) : 
        return self.total, self.gapyeong, self.pocheon

    def rename_df(self, df) : 
        df = df.rename(columns={"importance" : "🤜가격 산정"})
        df = df.rename(index={\
        'name': '이름(인지도)🌞',\
        'ranking': '리뷰 별점⭐',\
        'homepage': '홈페이지🌐',\
        'max_standard': '최대 인원수👥',\
        'roomname': '숙박🛏️',\
        'people_stadard': '표준 인원수👥',\

        'info_glamping': '글램핑🏕️',\
        'info_caravan': '카라반🚐',\
        'info_pension': '펜션🏘️',\
        'info_privatehouse': '전원주택🏡',\
        'info_poolvilla': '풀빌라🏊',\
        'info_bathroom': '개별 욕실🛁',\
        'info_terrace': '테라스🌳',\
        'info_deck': '테라스/데크🪑',\
        'info_spa': '스파/월풀/사우나/마사지💆‍♂️',\
        'info_grass': '잔디밭/초원🌿',\
        'info_unisex': '남녀공용화장실🚻',\
        'info_bogcheung': '복층식🏠',\
        'info_oceanview': '오션뷰🌊',\
        'info_ondolroom': '온돌/한옥🏯',\
        'info_partyroom': '파티룸🎉',\
        'info_womenonly': '여성 전용👩‍🦰',\
        'info_menonly': '남성 전용🧔',\
        
        'visitor_clean': '청결도🧼',\
        'visitor_view': '전망🌅',\
        'visitor_kind': '친절도🙂',\
        'visitor_bbq': '바베큐시설🍖',\
        'visitor_goodprice': '가성비👍',\
        'visitor_parking': '주차시설🅿️',\
        'visitor_publictransport': '대중교통🚉',\
        'visitor_hotwater': '온수/정수기🚰',\
        'visitor_waterplay': '수영장/물놀이시설🏊',\
        'visitor_maintainance': '유지보수🛠️',\
        'visitor_sink': '세탁기/식기세척기🧺',\
        'visitor_entertainment': '주변 관광지🏞️',\
        'visitor_photo': '사진 촬영📷',\
        'visitor_mannertime': '체크인/아웃 시간⏰',\
        'visitor_bathroom': '욕실청소상태🚽',\
        'visitor_interior': '인테리어/가구🛋️',\
        'visitor_bed': '침대/이불🛏️',\
        'visitor_bug': '벌레 조심🐛',\
        'visitor_child': '어린이 놀이시설🤸‍♀️',\
        'visitor_concept': '컨셉🎨',\
        'visitor_facility': '시설🚪',\
        'visitor_nearby': '인근 시설🏨',\
        'visitor_noise': '소음🔇',\
        'visitor_oceanview': '해변가🏖️',\
        'visitor_pet': '애완동물🐶',\
        'visitor_playground': '놀이터/운동시설🏋️‍♀️',\
        'visitor_pool': '수영장/물놀이시설🏊',\
        'visitor_rest': '휴식공간🧘‍♀️',\
        'visitor_shade': '그늘막/텐트/파라솔☂️',\
        'visitor_temperature': '온도/냉방/난방❄️',\
        'visitor_wide': '넓이/공간📏',\
        'visitor_worthy': '방문 가치💯', \
        'visitor_electricity': '전기⚡️'ㅎ
        })
        
        return df