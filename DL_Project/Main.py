import streamlit as st
import UI_UX
from UI_UX import UserInterface, UserExperience

def handle_ui() : return UserInterface()
def hadle_ux() : return UserExperience()

def main() : 
    UI_UX.set_page()
    ui = handle_ui()
    ux = hadle_ux()
    ux.set_BGM()

    df, direction = ui.choice_result()

    if df is not None : 
        ui.set_background()

        with st.sidebar : 
            ui.sidebar_print_df()
        
        if direction not in ["전체", "가평군", "포천시"] :
            ui.refactoring_ment()
        else:
            left_col, right_col = ui.set_column()

            with left_col : 
                ui.print_price()

            with right_col : 
                ui.result_ment()
                ui.cutting()
                ui.print_graph()
    else :
        ui.start_background()

if __name__ == '__main__' : 
    main()