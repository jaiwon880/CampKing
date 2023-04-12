import pandas as pd
import streamlit as st
# from pydub import AudioSegment

@st.cache
class GetData:
    def __init__(self) -> None : 
        # self.df_path = "DL_Project/Data_csv/glamping_data.csv"
        self.df_path = "DL_Project/Data_csv/df_final.csv"
        self.df = self.load_data()

    def load_data(self):
        try :  
            return pd.read_csv(self.df_path)
            
        except Exception as e : 
            return st.error(e)

    def create_data(self) : return self.df