import requests
import os


class User:
    # API URL
    baseURL = "https://vincentc.work/api"
    api_key = os.getenv("VINCENTWORK_PRO_KEY")
    headers = {
        "Authorizaton": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    def __init__(self):
        pass

    def add(self, username, email, password, gender, phone_number):
        fullURL = User.baseURL + "/auth/local/register"
        payload = {
            "username": username,
            "email": email,
            "password": password,
            "gender": gender,
            "role": "Public",
            "phone_number": phone_number,
        }
        try:
            r = requests.request(
                "POST",
                fullURL,
                headers=User.headers,
                data=payload,
            )
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e.response.text)

    def login(self, username, password):
        full_url = User.baseURL + "/auth/local"
        payload = {
            "identifier": username,
            "password": password,
        }
        try:
            r = requests.request("POST", full_url, headers=User.headers, data=payload)
            login_status = False
            user_detail = ""
            if r.status_code == 200:
                login_status = True
                user_detail = r.json()
            return login_status, user_detail

        except requests.exceptions.HTTPERROR as e:
            print(e.response.text)

    def update(user_id, **kwargs):
        payload = {}
        for key, value in kwargs.items():
            payload[key] = value

        full_url = User.baseURL + "/users/" + user_id

        try:
            r = requests.request(
                "PUT",
                full_url,
                headers=User.headers,
                data=payload,
            )
            if r.status_code == 200:
                return True
            else:
                print("Cannot find the user")

        except requests.exceptions.HTTPERROR as e:
            print(r.response.text)

    def reset_password(self):
        pass

    def forget_password(self):
        pass


if __name__ == "__main__":
    userSession = User()

    # vincent.add(
    #     username="vincent123456",
    #     email="vincenc.design+1@gmail.com",
    #     password="123456",
    #     gender="Male",
    #     phone_number="9999999",
    # )

    # login_status, user_detail = userSession.login(
    #     username="vincent123456", password="123456"
    # )
    # if login_status:
    #     print("You have logged in " + str(user_detail))

    # else:
    #     print("Wrong password or email")

    # User.update(user_id="12", gender="Male")
