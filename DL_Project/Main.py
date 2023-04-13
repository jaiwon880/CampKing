import UI as ui
import streamlit as st
import base64
import pickle
import matplotlib.pyplot as plt

from pydub.playback import play
from Functional import GetResult

def set_BGM():
    audio_path = "DL_Project/Data_csv/outdoor_crackling_fire_sound.mp3"
    audio_file = open(audio_path, 'rb').read()

    return st.markdown(f'<audio autoplay loop="true" src="data:audio/mp3;base64,\
                        {base64.b64encode(audio_file).decode()}"></audio>',\
                        unsafe_allow_html=True)

def get_search_result() : 
    return GetResult().get_result()

def main() : 
    ui.set_page()
    set_BGM()
    df, area, direction = get_search_result()

    if df is not None : 
        ui.set_background()
        # ui.title_ment(area, direction)

        with st.sidebar : 
            ui.sidebar_print_df(df)

        if direction == "가평군" :
            ui.print_direction("경기 가평군")
            ui.cutting()
            ui.gapyeong_load()
            
        elif direction == "포천시":
            ui.print_direction("경기 포천시")
            ui.cutting()
            GetResult().total_price()

        elif direction == "전체":
            ui.print_direction("전체")
            ui.cutting()
            ui.total_load()
    else : 
        ui.start_background()

if __name__ == '__main__' : 
    main()