import streamlit as st
import pandas as pd
import numpy as np

st.header(':blue[Police Incident Reports from 2018 to 2020 in San Francisco] :police_car: :us:')
df=pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")

st.markdown("The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.")

mapa=pd.DataFrame(df['Latitude'], df['Longitude'])
mapa=mapa.dropna()
st.map(mapa.astype(int))

st.write(f'Total Records: {len(df)}')
