import streamlit as st
import pandas as pd
import plotly.express as px


st.header("Weather Forecast for the Next Days")

# General Fields
place = st.text_input("Place:", placeholder="fill a place")
forcast_days = st.slider("Forcast Day", 1, 5)

# visal fields
visal_options = ["Temperature", "Sky"]
chosen_visual = st.selectbox("Select data to view", visal_options)

# Graph Area

st.subheader(f"Temperature for the next {forcast_days} days in {place or 'Somewhere'}")


def get_data(days):
    dates = ["2022-24-10", "2022-25-10", "2022-26-10"]
    temperatures = [23, 24, 26]
    temperatures = [forcast_days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperatures(c)"})
st.plotly_chart(figure)
