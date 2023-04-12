import pandas as pd
import streamlit as st

@st.cache
class GetData:
    def __init__(self) -> None : 
        # self.df_path = "DL_Project/Data_csv/glapingdata.csv"
        self.df_path = "DL_Project/Data_csv/final__data.csv"
        self.df = self.load_data()

        
    def load_data(self):
        try :  
            return pd.read_csv(self.df_path)
            
        except Exception as e : 
            return st.error(e)

    def create_data(self) : return self.df