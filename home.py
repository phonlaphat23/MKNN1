import streamlit as st
import pandas as pd

st.title("Website Developing using Python")
st.header("Website Developing using Python")

st.image('./img/photo.jpg')
st.subheader("Phonlahat Auitrakun")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.wite(dt.head(10))