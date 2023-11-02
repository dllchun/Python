import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


def get_html(url):
    # Request the html
    r = requests.get(url)
    content = r.text
    return content


def get_temperature_data(content):
    # Process the html
    soup = BeautifulSoup(content, "html.parser")
    temperature = soup.find("h1", id="temperatureId")
    temperature_text = temperature.text
    return temperature_text


def store_temperature(temperature):
    with open("file.txt", "a") as file:
        time = datetime.now()
        file.write(f"{time}, {temperature}\n")


def get_temperature(url):
    while True:
        content = get_html(url)
        temperature = get_temperature_data(content)
        store_temperature(temperature)
        time.sleep(30)
