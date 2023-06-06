import streamlit as st
import pandas as pd

st.title ('Police Incident Reports from 2018 and 2020 in San Francisco')
st.header('Introduction')

df = pd.read_csv("https://drive.google.com/file/d/1ioUp8979nNLh9h-CYVyJcRgAhxBhCLIm/view")

mapa=pd.DataFrame()
mapa=mapa.dropna()
st.map(mapa.astype(int))

st.write(f'Total Records: {len(df)}')
