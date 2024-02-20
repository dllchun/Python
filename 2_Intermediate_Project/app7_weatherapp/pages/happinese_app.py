import streamlit as st
import pandas as pd
import plotly.express as px


st.title("In Search fo Happinese")

x_label = st.selectbox(
    "Select the data for the X-axis", ["GDP", "Happiness", "Generosity"]
)

y_label = st.selectbox(
    "Select the data for the Y-axis", ["GDP", "Happiness", "Generosity"]
)

# Load Dataframe
df = pd.read_csv(
    "/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app7_weatherapp/happy.csv"
)

# Match Cases

match x_label:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]

match y_label:
    case "GDP":
        y_array = df["gdp"]
    case "Happiness":
        y_array = df["happiness"]
    case "Generosity":
        y_array = df["generosity"]

# x_data = df[x_label.lower()]
# y_data = df[y_label.lower()]


# Chart
st.subheader(f"{x_label} and {y_label}")
figure = px.scatter(x=x_array, y=y_array, labels={"x": x_label, "y": y_label})
st.plotly_chart(figure)
