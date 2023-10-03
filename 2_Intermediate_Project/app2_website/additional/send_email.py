import smtplib, ssl


def send_email(message="Hello", user_email="cwc210018111@gmail.com"):
    username = "wingchuncheung0108@gmail.com"
    password = "qdkehfaehenxvwat"

    host = "smtp.gmail.com"
    port = 465

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username, password)
        server.sendmail(username, user_email, message)
        server.quit()


send_email()
