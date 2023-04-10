import streamlit as st
# from pydub import AudioSegment
from Functional import GetResult
def set_page() : return st.set_page_config(page_title="DL", layout="wide")
def title_message() : return st.error("## TDD - Testing..."), st.markdown("---")

def get_df() : return GetResult().get_result()
# def audio() : return GetResult().get_audio()

def user_interface():
    set_page()
    
    df, area, direction, address = get_df()

    if df is not None : title_message()
    
    with st.sidebar : 
        if df is not None : st.write("일치하는 업체가 없습니다.") if df.empty else st.dataframe(df, width=700)
 
    with st.container():
        if area is not "" and direction is not ("" and None) :
            st.write(f"""
                        ### 선택한 결과 입니다. 👉{area} {direction} {address}
            """)
    
    with st.expander("# 메커니즘_설명 / 용량이 엄청 클 것 으로 예상 되기에 백엔드적으로도 줄여서 하기 위함. "):
        st.image("https://i.imgur.com/SgRVHOk.jpg", width = 1000)

    # image = [
    #     "https://i.imgur.com/t4O7ozH.jpg", 
    #     "https://i.imgur.com/idnsDBs.gif", 
    #     "https://i.imgur.com/fvRG1Tj.gif"
    #     ]

    # for i in range(len(image)) :
    #     with st.expander(f"사진_{i+1}"):
    #         st.image(image[i])


    # containers = [st.container() for i in range(len(image))]
    # for i in range(len(image)) :
    #     with containers[i] : 
    #         st.image(image[i], width = 700)
    # # =====================================================================
    # messages = ['success', 'info', 'warning', 'error']

    # for i in range(3):
    #     for message in messages:
    #         getattr(st, message)(f'{message} 메세지')