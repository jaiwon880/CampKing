import streamlit as st
import pandas as pd


def main():
    df = pd.read_csv("DL_Project/Data_csv/glamping_after.csv")
    df = df.head()
    st.dataframe(df)
main()