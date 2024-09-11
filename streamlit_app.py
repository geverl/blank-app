import streamlit as st

st.title("🎈 My first Streamlit steps")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40],
  'third column': [10, 20, 30, 40]
})

df
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)