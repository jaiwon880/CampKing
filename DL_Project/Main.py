import UI
import streamlit as st
from ChoiceArea import GetSideBar

def main() : 
   if GetSideBar().area_choice != "" : 
      UI.user_interface()
   else :
      st.image("https://i.imgur.com/fvRG1Tj.gif")
# 메인 실행
if __name__ == '__main__' : 
   main()