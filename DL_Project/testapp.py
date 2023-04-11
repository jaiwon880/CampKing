import streamlit as st
import pandas as pd


def main():
    df = pd.read_csv("DL_Project/Data_csv/glamping_after.csv")
    
    st.dataframe(df)
main()