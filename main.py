import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_data

st.title("Weather forecast for the next days")
# df.pd.read_csv

place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5, help='Select the number of forecasted days')

option = st.selectbox("Select data to view", ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} days in {place}')

data = get_data(place, days, option)

d, t = get_data()

figure = px.line(x=dates, y=temperatures, labels={"x": "DATE", "y": "Temperature C`"})
st.plotly_chart(figure)


