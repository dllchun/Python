import streamlit as st
from send_email import send_email
import pandas

st.header("contact us")

with open("topics.csv") as topic_file:
    print(topic_file.read())


with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Message")
    topics = st.selectbox("How would you like to talk about", ("Email", "Email"))
    message = f"""
    Subject: New email from {user_email}
    From: {user_email}
    {raw_message}
    """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message=message, user_email=user_email)
        st.info("Your email was sent successfully")
