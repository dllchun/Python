import streamlit as st
from main import get_temperature
import pandas as pd
import plotly.express as px
import time


st.header("Real-time Temperature")

df = pd.read_csv(
    "file.txt",
    sep=",",
    parse_dates=["date"],
)
date = df["date"]
temp = df[" temperature"]


figure = px.line(x=date, y=temp)
st.plotly_chart(figure)

get_temperature("https://programmer100.pythonanywhere.com/")
