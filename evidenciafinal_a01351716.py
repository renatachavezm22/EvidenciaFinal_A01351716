import streamlit as st
import pandas as pd
import folium

st.title('Police Incident Reports from 2018 and 2020 in San Francisco')

df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")
st.dataframe(df)

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

for index, row in df.iterrows():
    if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
        folium.Marker([row['Latitude'], row['Longitude']]).add_to(mapa)

st.map(mapa)
