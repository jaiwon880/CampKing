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

def print_this(direction) : 
    return ui.print_direction(direction), ui.cutting()

def main() : 
    ui.set_page()
    set_BGM()

    get = GetResult()
    df, area, direction = get.get_result()

    if df is not None : 
        ui.set_background()

        with st.sidebar : 
            ui.sidebar_print_df(df)

        if direction == "가평군" :
            print_this("경기 가평군")
            get.gapyeong_price()
            
        elif direction == "포천시":
            print_this("경기 포천시")
            get.pocheon_price()

        elif direction == "전체":
            print_this("전체")
            get.total_price()
        else : df.empty
    else : 
        ui.start_background()

if __name__ == '__main__' : 
    main()