import UI as ui
import streamlit as st
import base64
import pickle
import matplotlib.pyplot as plt

from pydub.playback import play
from Functional import GetResult  

def main() : 
    ui.set_page()
    ui.set_BGM()

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