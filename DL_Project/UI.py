import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def cutting() : 
    return st.markdown("---")

def set_page() : 
    return st.set_page_config(page_title="for Doksan Seo teacher", page_icon="🏕️", layout="wide", \
                                initial_sidebar_state="expanded")

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

def print_direction(direction) : 
    return st.markdown(f"<div style='background-color: green; \
                        padding: 10px; color: white; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{direction} \
                        </div>", unsafe_allow_html=True)

def refactoring() : 
    ment = "사용자 에게 도출될 키워드 리뷰 카운드(%별 수), 업체 사진(image), 객실 정보(info) 등은 한글 화 진행 중 추후 리팩토링.."
    return st.markdown(f"<div style='background-color: white; \
                        padding: 10px; color: green; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{ment} \
                        </div>", unsafe_allow_html=True)

def sidebar_print_df(df) :
    return st.write("업체가 충분하지 않거나 없습니다.") if len(df) < 10 else st.write("# Best!"), st.dataframe(df.head(), width=600), \
                                                                            st.write("# Worst!"), st.dataframe(df.tail(), width=600)