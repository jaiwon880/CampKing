import requests
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np

# import plotly.graph_objects as go
# import plotly.express as px
# import matplotlib.pyplot as plt 

# 중앙 정렬
st.set_page_config(layout="wide") 
# 단일 컬럼 생성
col1, col2 = st.columns([8, 2])
# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.... 
tab1, tab2= st.tabs(['필기 년도 별 합격률' , '응시자 및 합격자 수'])


# 데이터 프레임 생성
def create_df():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
  df_URL_g_1 = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EA%B7%B8%EB%9E%98%ED%94%84_1.csv"
  
  # df을 읽어 오면서 df언네임 삭제
  df = pd.read_csv(df_URL).iloc[:, 1:]
  df_g_1 = pd.read_csv(df_URL_g_1)

  # df인덱스 올림       
  df.index += 1

  # df 반환
  return df, df_g_1


# 사이드바
def side_bar(df) :
  # 사이드바 생성 : st.sidebar를 s_bar 로 간추리기
  s_bar = st.sidebar

  # 지역 선택 멘트 타이틀
  s_bar.title('지역을 선택해주세요.')

  # area에 df에서 열 중에서 지사명인 열에 값들을 중복을 제거하고 리스트로 변환
  area = df['지사명'].drop_duplicates().tolist()

  # choice라는 변수에 셀렉트박스의 값에서 선택된 값들을 저장
  choice = s_bar.selectbox('지역 선택(재검색시 상세 검색을 지워 주세요)', area, index = 10)

  # 위 area 리스트의 크기 만큼 반복 그냥 if문을 area의 리스트 크기만큼 작성
  for i in range(len(area)):
    # 초이스 셀렉트바에서 선택한 값이 area의 인덱스 값과 일치한다면
    if choice == area[i]: 
      result = df[df['지사명'] == area[i]] # result에 지사명이 지역을 선택한 값들의 데이터들은 저장
    else : pass
   
  # 검색바 만들기
  search = s_bar.text_input('상세 검색 \n (시, 교명등의 키워드를 입력 :smile:)')

  # 지역선택한 값안에서 시험장소를 검색(입력)한 값과 일치하는 값을 담는다.
  result = df[(df['지사명'] == choice) & (df['시험장소'].str.contains(search))]

  # result 데이터프레임의 인덱스를 1부터 시작하도록 변경 
  result.index = np.arange(1, len(result) + 1) 

  return df, result # 데이터프레임과 지역선택의 값을 return 

def create_graph(image_url):
  image = Image.open(requests.get(image_url, stream=True).raw)
  return image

def main():
  # df 생성 및 함수 호출
  df, df_g_1 = create_df() 
  # 사이드 바 함수를 호출해서 df, result값을 반환 받는다.
  df, result = side_bar(df) 

  with col1 :
    # column 에 담을 내용
    
    # 제목
    st.title(':smile: 시험장소를 안내해드립니다 :smile:') 
    
    # 데이터프레임 출력 및 사이즈 조절
    st.dataframe(result, width=800, height=500)

    # 부제목
    st.subheader(":smile: 귀하의 합격을 기원합니다! :smile:")

  with col2 :
    # 지도 아이콘 하이퍼링크 네이버 
    st.markdown("[![Foo](https://i.imgur.com/SywJPmA.png)](https://map.naver.com/)")

  with tab1 :
    # tab1 에 담을 내용 // 그래프 1
    image_url = "https://i.imgur.com/wOY7lUx.png"
    st.image(create_graph(image_url), use_column_width=True)
    
  with tab2 :
    # tab2 에 담을 내용
    image_url = "https://i.imgur.com/C9nrLkC.png"
    st.image(create_graph(image_url), use_column_width=True)
    
if __name__ == '__main__':
  main()