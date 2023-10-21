import streamlit as st
import pandas as pd
import plotly.express as px
import requests as r
from backend import get_data


st.header("Weather Forecast for the Next Days")

# General Fields
place = st.text_input("Place:", placeholder="fill a place")
forecast_days = st.slider("Forcast Day", 1, 5)

# visal fields
visal_options = ["Temperature", "Sky"]
options = st.selectbox("Select data to view", visal_options)

# Graph Area

st.subheader(f"Temperature for the next {forecast_days} days in {place or 'Somewhere'}")


# Get the temperature data
if place:
    try:
        filtered_data = get_data(place, forecast_days)

        # Create the visualisation
        if options == "Temperature":
            temps = [round(dict["main"]["temp"] / 10, 2) for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(
                x=dates, y=temps, labels={"x": "Date", "y": "Temperatures(c)"}
            )
            st.plotly_chart(figure)

        if options == "Sky":
            conditions = [dict["weather"][0]["main"] for dict in filtered_data]

            images = {
                "Clear": "/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app7_weatherapp/images_2/clear.png",
                "Clouds": "/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app7_weatherapp/images_2/cloud.png",
                "Rain": "/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app7_weatherapp/images_2/rain.png",
                "Snow": "/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app7_weatherapp/images_2/snow.png",
            }
            condition_image_list = [images[condition] for condition in conditions]
            st.image(condition_image_list, width=115)

    except KeyError:
        st.write("That place does not exit")
    except TypeError:
        st.write("That place does not exit")
