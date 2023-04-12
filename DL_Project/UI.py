import streamlit as st
import base64
from Functional import GetResult
from pydub.playback import play

def set_page() : return st.set_page_config(page_title="DL", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")
    
def set_background() : return st.markdown("""
    <style>
    .main {
        background-image: url('https://i.imgur.com/PSeW0pm.gif');
        background-size: cover;
        }
    </style> """, unsafe_allow_html=True)

def start_background() : return st.markdown("""
    <style>
    .main {
        background-image: url('https://i.imgur.com/idnsDBs.gif');
        background-size: cover;
        }
    </style> """, unsafe_allow_html=True)
    
    
    # return st.image("https://i.imgur.com/idnsDBs.gif", width = 1200)

def get_df() : return GetResult().get_result()

def sidebar_print_df(df) : return st.dataframe(df, width=500)

def title_ment(area, direction) : return st.error(f"# 👉{area} {direction}"), st.markdown("---")

# def search_result(area, direction) : return st.write(f"### 선택한 결과 입니다. ") 

# def mecanism_ment() : return "# 메커니즘_설명 / 용량이 엄청 클 것 으로 예상 되기에 메모리 최적화. "
# def mechanism_image() : return st.image("https://i.imgur.com/SgRVHOk.jpg", width = 1000)

# def image() : return ["https://i.imgur.com/t4O7ozH.jpg", "https://i.imgur.com/idnsDBs.gif", "https://i.imgur.com/fvRG1Tj.gif"]
# def containers() : return [st.container() for i in range(len(image()))]
    # for i in range(len(image())) :
    #         with containers()[i] : st.image(image()[i], width = 700)
    
def user_interface():
    set_page()
    
    df, area, direction = get_df()

    audio_file = open('DL_Project/Data_csv/outdoor_crackling_fire_sound.mp3', 'rb').read()
    st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{base64.b64encode(audio_file).decode()}"></audio>',unsafe_allow_html=True)

    if df is not None : 
        # set_background()
        title_ment(area, direction)
        with st.sidebar : sidebar_print_df(df)
        # with st.expander(mecanism_ment()) : mechanism_image()
        
        
        
    else : 
        start_background()
        
     
        































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