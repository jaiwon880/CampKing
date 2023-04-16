import streamlit as st
import base64
from pydub.playback import play

def set_BGM():
    try:
        audio_path = "DL_Project/Data_csv/outdoor_crackling_fire_sound.mp3"
        audio_file = open(audio_path, 'rb').read()

        st.markdown(f'<audio autoplay loop="true" src="data:audio/mp3;base64,\
                    {base64.b64encode(audio_file).decode()}"></audio>',\
                    unsafe_allow_html = True)          
    except Exception as e : 
            return st.error(e)

def cutting() : 
    st.markdown("---")

def set_page() : 
    st.set_page_config(page_title="for Doksan Seo teacher",\
                        page_icon="🏕️", \
                        layout="wide", \
                        initial_sidebar_state="auto", \
                        )
    # 사이드바 배경색 변경
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #f0f0f0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 사이드바 글꼴 색상 변경
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3, .sidebar .sidebar-content h4, .sidebar .sidebar-content h5, .sidebar .sidebar-content h6, .sidebar .sidebar-content a {
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def set_background():
    # https://t1.daumcdn.net/cfile/blog/99C6924C5B65B8BD02
    # https://i.imgur.com/PSeW0pm.gif
    st.markdown("""<style>
                .main {
                        background-image: url('https://t1.daumcdn.net/cfile/blog/99C6924C5B65B8BD02');
                        background-size: cover;
                    }
                    </style> """, unsafe_allow_html=True)

def start_background() : 
    st.markdown("""<style>
                .main {
                        background-image: url('https://i.imgur.com/idnsDBs.gif');
                        background-size: cover;
                    }
                </style> """, unsafe_allow_html=True)

def title_ment(area, direction, count) : 
    st.markdown(f"<div style='background-color: green; \
                    padding: 10px; color: white; font-size: 48px;\
                    font-weight: bold; display: inline-block;'> \
                    👉{area} {direction} {count}곳 의 업체 결과\
                    </div>", unsafe_allow_html=True)

def refactoring_ment() : 
    ment = "업체가 10개 미만입니다. 분석에 의미가 없습니다."
    st.markdown(f"<div style='background-color: white; \
                padding: 10px; color: green; font-size: 48px;\
                font-weight: bold; display: inline-block;'> \
                👉{ment} \
                </div>", unsafe_allow_html=True)

def sidebar_print_df(df) :
    if len(df) > 10 :
        st.write("# Best!"), st.dataframe(df.head(), width=600)
        st.write("# Worst!"), st.dataframe(df.tail(), width=600)

    else : 
        st.write("분석할 업체의 수 가 충분하지 않습니다.")