import UI as ui
import streamlit as st
import base64
import pickle

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

# def get_df() : 
#     return GetResult().just_df()

def sidebar_print_df(df) :
    return st.write("업체가 충분하지 않거나 없습니다.") if len(df) < 10 else st.write("# Best!"), st.dataframe(df.head(), width=600), \
                                                                            st.write("# Worst!"), st.dataframe(df.tail(), width=600)
def main() : 
    ui.set_page()
    set_BGM()
    df, area, direction = get_search_result()

    if df is not None : 
        ui.set_background()
        ui.title_ment(area, direction)
        ui.cutting()

        with st.sidebar : 
            sidebar_print_df(df)

        ui.result_chart()
        ui.cutting()
        gapyeong = ui.gapyung_load()

        # st.write(gapyeong.summary())
        # st.write(pocheon.summary())
        # st.write(total.summary())

        # containers = [st.container() for i in range(len(df.head()))]
        # for i in range(len(df.head())) :
        #     with containers[i]:
        #         st.write(df.loc[i, 1])

    else : ui.start_background()

if __name__ == '__main__' : 
    main()