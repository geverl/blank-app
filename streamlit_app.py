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
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
