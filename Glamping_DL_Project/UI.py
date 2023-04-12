import streamlit as st
from Data import GetData
def get_data() : return GetData().create_data()
def user_interface():
    
    st.title("독산 서선생의 서시.....")
    st.dataframe(get_data())