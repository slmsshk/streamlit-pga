import streamlit as st
from sklearn.datasets import load_iris

st.write('hello world')
st.write('GM')
st.balloons()

data = load_iris(as_frame=True).frame

st.write(data.head())

