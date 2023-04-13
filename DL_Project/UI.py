import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def set_page() : 
    return st.set_page_config(page_title="DL", page_icon=":smiley:", layout="wide")

def set_background():
    return st.markdown("""<style>
                        .main {
                            background-image: url('https://i.imgur.com/PSeW0pm.gif');
                            background-size: cover;
                        }
                        </style> """, unsafe_allow_html=True)


def start_background() : 
    return st.markdown("""<style>
                        .main {
                            background-image: url('https://i.imgur.com/idnsDBs.gif');
                            background-size: cover;
                        }
                        </style> """, unsafe_allow_html=True)

def title_ment(area, direction) : 
    return st.markdown(f"<div style='background-color: green; \
                        padding: 10px; color: white; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{area} {direction} \
                        </div>", unsafe_allow_html=True)

def cutting() : 
    return st.markdown("---")

def total_load():
    total = pd.read_csv("DL_Project/Data_csv/total.csv",index_col =0, encoding="utf-8")

    total_ranking_keyword = total['importance'][:11].transpose()

    fig, ax = plt.subplots(figsize=(10, 8))
    total.plot(kind='barh', ax=ax)

    return st.pyplot(fig), st.write(total_ranking_keyword)

def total_image() : 
    return st.image("https://i.imgur.com/qZJvwRB.png"), \
            st.image("https://i.imgur.com/Bgv83pb.png"), \
            st.image("https://i.imgur.com/QGxbZJa.png")

def refactoring() : 
    ment = "사용자 에게 도출될 키워드 리뷰 카운드(%별 수), 업체 사진(image), 객실 정보(info) 등은 한글 화 진행 중 추후 리팩토링.."
    return st.markdown(f"<div style='background-color: white; \
                        padding: 10px; color: green; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{ment} \
                        </div>", unsafe_allow_html=True)

def this_direction(direction) : 
    ment = "사용자 에게 도출될 키워드 리뷰 카운드(%별 수), 업체 사진(image), 객실 정보(info) 등은 한글 화 진행 중 추후 리팩토링.."
    return st.markdown(f"<div style='background-color: white; \
                        padding: 10px; color: green; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{ment} \
                        </div>", unsafe_allow_html=True)