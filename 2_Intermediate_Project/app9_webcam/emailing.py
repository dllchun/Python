import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def send_email(image_path):
    username = "wingchuncheung0108@gmail.com"
    password = "qdkehfaehenxvwat"

    msg_root = MIMEMultipart("related")
    msg_root["Subject"] = "test message"
    msg_root["From"] = username
    msg_root["To"] = "cwc210018111@gmail.com"

    msg_text = MIMEText("test message")
    msg_root.attach(msg_text)

    with open(image_path, "rb") as image:
        msg_image = MIMEImage(image.read())

    msg_image.add_header("Content-Type", "<image1>")
    msg_root.attach(msg_image)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(username, "cwc210018111@gmail.com", msg_root.as_string())


if __name__ == "__main__":
    send_email("2_Intermediate_Project/app9_webcam/images/5.png")
