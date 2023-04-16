import streamlit as st
 
def cutting() : 
    st.markdown("---")

def set_page() : 
    st.set_page_config(page_title="for Doksan Seo teacher", page_icon="🏕️", layout="wide", \
                        initial_sidebar_state="expanded")

def set_background():
    st.markdown("""<style>
                .main {
                        background-image: url('https://i.imgur.com/PSeW0pm.gif');
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