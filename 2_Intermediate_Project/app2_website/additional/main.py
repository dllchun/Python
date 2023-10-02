import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")
subheading = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
st.write(subheading)

st.write("Our Team")

df = pd.read_csv("new_data.csv", sep=",")
for index, row in df.iterrows():
    print(row["first name"])


col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()} ')
        st.write(row["role"])
        st.image(f'images/{row["image"]}')

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()} ')
        st.write(row["role"])
        st.image(f'images/{row["image"]}')

with col3:
    for index, row in df[8:].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()} ')
        st.write(row["role"])
        st.image(f'images/{row["image"]}')
