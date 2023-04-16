import streamlit as st
import UI_UX
from UI_UX import User_Interface, User_Experience
from Functional import GetResult  

def main() : 
    UI_UX.set_page()
    ui = User_Interface()
    ux = User_Experience()
    ux.set_BGM()

    get = GetResult()
    df, area, direction = get.choice_result()

    if df is not None : 
        # ui.set_background()

        with st.sidebar : 
            ui.sidebar_print_df(df)
        
        if direction == "전체" or direction == "가평군" or direction == "포천시" :
            ui.title_ment(area, direction, len(df))
            ui.cutting()
            get.price_result()

        else : ui.refactoring_ment()
    else : ui.start_background()

if __name__ == '__main__' : 
    main()