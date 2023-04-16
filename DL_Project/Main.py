import UI as ui, ux
import streamlit as st
import base64
import pickle
import matplotlib.pyplot as plt

from pydub.playback import play
from Functional import GetResult

def set_BGM():
    audio_path = "DL_Project/Data_csv/outdoor_crackling_fire_sound.mp3"
    audio_file = open(audio_path, 'rb').read()

    st.markdown(f'<audio autoplay loop="true" src="data:audio/mp3;base64,\
                {base64.b64encode(audio_file).decode()}"></audio>',\
                unsafe_allow_html = True)    

def main() : 
    ui.set_page()
    set_BGM()

    get = GetResult()
    df, area, direction = get.get_choice_result()

    if df is not None : 
        ui.set_background()

        with st.sidebar : 
            ui.sidebar_print_df(df)
        
        if direction == "전체" or direction == "가평군" or direction == "포천시" :
            ui.title_ment(area, direction, len(df))
            ui.cutting()
            get.get_price()

        else : ui.refactoring()
    else : ui.start_background()

if __name__ == '__main__' : 
    main()