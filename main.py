import streamlit as st
import pandas as pd
import plotly.express as px

# Google Drive 파일 다운로드 링크
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv(url)
    return df

df = load_data()

st.title("데이터 시각화 웹앱 (Plotly + Streamlit)")
st.write("아래는 업로드된 데이터를 Plotly로 시각화한 것입니다:")

# 데이터프레임 확인
st.dataframe(df)

# 컬럼 선택
numeric_columns = df.select_dtypes(include='number').columns.tolist()

x_axis = st.selectbox("X축 선택", numeric_columns)
y_axis = st.selectbox("Y축 선택", numeric_columns)

# Plotly 그래프
if x_axis and y_axis:
    fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    st.plotly_chart(fig)
