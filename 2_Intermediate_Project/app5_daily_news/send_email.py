import smtplib


def send_email(message):
    username = "wingchuncheung0108@gmail.com"
    password = "qdkehfaehenxvwat"

    port = 465
    host = "smtp.gmail.com"

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username, password)
        server.sendmail(username, "cwc210018111@gmail.com", message)
