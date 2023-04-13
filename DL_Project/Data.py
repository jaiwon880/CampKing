import pandas as pd
import streamlit as st
import pickle

@st.cache
class GetData:
    def __init__(self) -> None : 
        self.path = ["DL_Project/Data_csv/df_final.csv",\
                    "DL_Project/Data_csv/total.csv",\
                    "DL_Project/Data_csv/gapyeong.csv",\
                    "DL_Project/Data_csv/pocheon.csv"]

        self.df = self.load_data()
        self.total, self.gapyeong, self.pocheon = self.load_area_price()

    def load_data(self):
        try :  
            return pd.read_csv(self.path[0])
        except Exception as e : 
            return st.error(e)

    def load_area_price(self) :
        try:
            return pd.read_csv(self.path[1], index_col =0, encoding="utf-8"),\
                    pd.read_csv(self.path[2], index_col =0, encoding="utf-8"),\
                    pd.read_csv(self.path[3], index_col =0, encoding="utf-8")

        except Exception as e:
            return st.error(e)

    def create_data(self) : return self.df, self.total, self.gapyeong, self.pocheon