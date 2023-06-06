import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title ('Police Incident Reports from 2018 and 2020 in San Francisco')
st.header('Police Incident Reports from 2018 and 2020 in San Francisco')

df = pd.read_csv("https://drive.google.com/file/d/1ioUp8979nNLh9h-CYVyJcRgAhxBhCLIm/view")

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa=pd.DataFrame()
mapa=mapa.dropna()
st.map(mapa.astype(int))

