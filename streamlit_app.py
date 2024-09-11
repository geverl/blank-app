import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My first Streamlit steps")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40],
  'third column': [10, 20, 30, 40]
})

df

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.text_input("Your name", key="name")
st.session_state.name