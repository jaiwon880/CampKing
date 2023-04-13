import pandas as pd
import streamlit as st
import pickle
# from pydub import AudioSegment

@st.cache
class GetData:
    def __init__(self) -> None : 
        # self.df_path = "DL_Project/Data_csv/glamping_data.csv"
        self.df_path = "DL_Project/Data_csv/df_final.csv"
        self.df = self.load_data()

        # self.pkl_gapyeong_path = "DL_Project/Data_csv/autogluon_gapyeong.pkl"
        # self.pkl_pocheon_path = "DL_Project/Data_csv/autogluon_pocheon.pkl"
        # self.pkl_total = "DL_Project/Data_csv/autogluon_total.pkl"
        # self.pkl_gapyeong, self.pkl_pocheon, self.pkl_total = self.load_pkl()

    def load_data(self):
        try :  
            return pd.read_csv(self.df_path)
        except Exception as e : 
            return st.error(e)

    # def load_pkl(self) : 
    #     with open(self.pkl_gapyeong, 'rb') as gapyeong, open(self.pkl_pocheon_path, 'rb') as pocheon, open(self.pkl_total, 'rb') as total:
    #         return pikle.load(gapyeong), pikle.load(pocheon), pikle.load(total)

    def create_data(self) : return self.df