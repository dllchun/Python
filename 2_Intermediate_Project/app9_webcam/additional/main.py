import streamlit as st
import cv2
from datetime import datetime

st.title("Motion Detectors")
start_button = st.button("Start Camera")


if start_button:
    st_image_list = st.image([])
    camera = cv2.VideoCapture(1)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        now = datetime.now()

        cv2.putText(
            img=frame,
            text=now.strftime("%A"),
            org=(30, 80),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=3,
            color=(255, 255, 255),
            thickness=2,
            lineType=cv2.LINE_AA,
        )

        cv2.putText(
            img=frame,
            text=now.strftime("%H:%M:%S"),
            org=(30, 140),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=3,
            color=(255, 0, 0),
            thickness=2,
            lineType=cv2.LINE_AA,
        )

        st_image_list.image(frame)
