import UI as ui
import streamlit as st
from Functional import GetResult

def get_search_result() : 
    return GetResult().get_result()

def sidebar_print_df(df) : 
    return st.dataframe(df, width=600)

def main() : 
    ui.set_page()
    ui.set_BGM()

    df, area, direction = get_search_result()

    if df is not None : 
        ui.set_background()
        ui.title_ment(area, direction)
        ui.cutting()

        with st.sidebar : 
            sidebar_print_df(df)

        ui.result_chart()
    
        # containers = [st.container() for i in range(len(df.head()))]
        # for i in range(len(df.head())) :
        #     with containers[i]:
        #         st.write(df.loc[i, 1])

    else : 
        ui.start_background()

if __name__ == '__main__' : 
    main()