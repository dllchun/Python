import smtplib
from email.message import EmailMessage
import imghdr


def send_email(image_path):
    username = "wingchuncheung0108@gmail.com"
    password = "qdkehfaehenxvwat"

    message = EmailMessage()
    message["Subject"] = "New cutomer showed up!"
    message.set_content("Hey, we ust saw a new customer")

    with open(image_path, "rb") as file:
        content = file.read()

    message.add_attachment(
        content, maintype="image", subtype=imghdr.what(None, content)
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(username, "cwc210018111@gmail.com", message)


if __name__ == "__main__":
    send_email("2_Intermediate_Project/app9_webcam/images/5.png")
