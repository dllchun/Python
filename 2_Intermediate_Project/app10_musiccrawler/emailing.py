import smtplib
from dotenv import load_dotenv
import os


load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(username, "cwc210018111@gmail.com", message)


if __name__ == "__main__":
    send_email("123")
