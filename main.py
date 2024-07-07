import streamlit as st
import plotly.express as px
from backend import get_data


# Widget settings
st.title("Weather forecast for the next days")

place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5, help='Select the number of forecasted days')

option = st.selectbox("Select data to view", ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} days in {place}')


try:
    if place:
        # Get temperature / sky data
        filtered_data = get_data(place, days)
        date = [dict['dt_txt'] for dict in filtered_data]

        if option == "Temperature":
            # Create temperature plot
            temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
            figure = px.line(x=date, y=temperatures, labels={"x": "Date", "y": "Temperature C`"})
            st.plotly_chart(figure)

        if option == "Sky":
            # Create sky images
            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            st.columns(4)
            for image, day in zip(sky_condition, date):
                image = image.lower()
                st.image(f"images/{image}.png", width=115)
                st.write(day)
except (KeyError, IndexError, TypeError) as e:
    st.info('Not existing place')






