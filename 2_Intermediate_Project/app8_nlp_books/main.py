import streamlit as st
from get_pos import get_score
import plotly.express as px

# Load Data

pos_list, neg_list, date_list = get_score()


# Streamlit Setting

st.header("Diary Tone")

# Postivity Chart
st.subheader("Positivity")
figure = px.line(x=date_list, y=pos_list, labels={"y": "Postivity", "x": "Date"})
st.plotly_chart(figure)

# Negativity Chart
st.subheader("Negativity")
figure = px.line(x=date_list, y=neg_list, labels={"y": "Negativity", "x": "Date"})
st.plotly_chart(figure)
