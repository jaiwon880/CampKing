import streamlit as st
import UI_UX
from UI_UX import User_Interface, User_Experience

def handle_ui() : return User_Interface()
def hadle_ux() : return User_Experience()

def main() : 
    UI_UX.set_page()
    
    hadle_ux().set_BGM()

    ui = handle_ui()
    df, direction = ui.choice_result()

    if df is not None : 
        # ui.set_background()

        with st.sidebar : ui.sidebar_print_df()
        
        if direction == "전체" or direction == "가평군" or direction == "포천시" :
            ui.title_ment()
            ui.cutting()
            ui.price_print()

        else : ui.refactoring_ment()
    else : ui.start_background()

if __name__ == '__main__' : 
    main()