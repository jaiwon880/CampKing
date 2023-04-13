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

        self.pkl_gapyeong_path = "DL_Project/Data_csv/autogluon_gapyeong.pkl"
        elf.pkl_gapyeong = self.load_pkl()

    def load_data(self):
        try :  
            return pd.read_csv(self.df_path)
        except Exception as e : 
            return st.error(e)

    def load_pkl(self) : 
        with open(self.pkl_gapyeong_path, 'rb') as f:
            file_path = "example.pkl"
            return pickle.load(f)

    def create_data(self) : return self.df