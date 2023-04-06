import streamlit as st
st.set_page_config(page_title="DL", layout="wide")

def user_interface():
    st.title("뼈대 작업 중...")
    
    image = ["https://i.imgur.com/t4O7ozH.jpg", "https://i.imgur.com/idnsDBs.gif", "https://i.imgur.com/fvRG1Tj.gif"]
    
    containers = [st.container() for i in range(len(image))]
    
    for i in range(len(image)) :
        with containers[i] : 
            st.image(image[i], width = 700)