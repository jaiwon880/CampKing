import streamlit as st
from session_state import get_state
import UI

def main():
    # SessionState 초기화
    state = get_state()

    # 이미지 출력
    img_url = "https://i.imgur.com/fvRG1Tj.gif"
    st.image(img_url, use_column_width=True, on_click=state.__setitem__, args=("button_clicked", True))

    # 버튼을 클릭하면 UI.user_interface() 함수를 호출하는 이벤트 처리
    if state.get("button_clicked", False):
        # SessionState 초기화
        state.__setitem__("button_clicked", False)
        UI.user_interface()

if __name__ == '__main__':
    main()



# import streamlit as st
# import UI

# def main() : 
#     UI.user_interface()

# if __name__ == '__main__' : 
#     main()