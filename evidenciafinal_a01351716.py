 import streamlit as st
import pandas as pd
#import numpy as np
#import plotly as px
#import plotly.figure_factory as ff
#from bokeh.plotting import figure
#import matplotlib.pyplot as plt

st.title ('Police Incident Reports from 2018 and 2020 in San Francisco')

df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")
st.dataframe(df)
st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa=pd.DataFrame()
mapa['Date']=df['Incident Date']
mapa['Day']=df['Incident Day of the Week']
mapa['Police District']=df['Police District']
mapa['Neighborhood']=df['Analysis Neoghborhood']
mapa['Incident Category']=df['Incident Category']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()
st.map(mapa.astype(int))
