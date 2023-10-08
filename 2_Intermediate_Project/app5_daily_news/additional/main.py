import streamlit as st
import requests as r

# API info

api_key = "lraYAxtSweb8QehqJFpI3VmRDcsKBVnWtqS8Aume"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
# Make API request

request = r.get(url)
content = request.json()

# Stroe variable
img_url = content["url"]
title = content["title"]
description = content["explanation"]

# Process image

img_response = r.get(img_url)
real_img_content = img_response.content

with open("image.jpg", "wb") as img:
    real_img = img.write(real_img_content)

# Streamlit setup

st.header(str(title))
st.image("image.jpg")
st.write(str(description))
