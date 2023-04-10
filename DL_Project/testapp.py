import streamlit as st
import pandas as pd


def load_data(self):
    try :  
        return pd.read_csv("DL_Project/Data_csv/glapingdata.csv")
        
    except Exception as e : 
        return st.error(e)

def main():
    df = load_data()
    df = df.head()
    st.dataframe(df)
main()