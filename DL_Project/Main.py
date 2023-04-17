import streamlit as st
import UI_UX
from UI_UX import User_Interface, User_Experience

def handle_ui() : return User_Interface()
def hadle_ux() : return User_Experience()

def main() : 
    UI_UX.set_page()
    hadle_ux().set_BGM()

    ui = handle_ui()
    ui.get_col()

    df, direction = ui.choice_result()

    if df is not None : 
        ui.set_background()

        with st.sidebar : ui.sidebar_print_df()
        
        if direction not in ["전체", "가평군", "포천시"] :
            ui.refactoring_ment()
        else:
            with left_col :
                ui.title_ment()
                ui.cutting()
                ui.print_graph()
            with right_co2 :
                ui.print_df()
    else : 
        ui.start_background()

if __name__ == '__main__' : 
    main()