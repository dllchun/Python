import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

db_path = "2_Intermediate_Project/app10_musiccrawler/data.db"

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()


def get_html(url):
    # Request the html
    r = requests.get(url)
    content = r.text

    # Process the html
    soup = BeautifulSoup(content, "html.parser")
    temperature = soup.find("h1", id="temperatureId")
    temperature_text = temperature.text
    return temperature_text


def store_temperature(temperature):
    time = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor.execute("INSERT INTO temperature VALUES(?,?)", (time, temperature))
    conn.commit()


def get_temperature(url):
    while True:
        content = get_html(url)
        temperature = get_temperature_data(content)
        store_temperature(temperature)
        time.sleep(30)


if __name__ == "__main__":
    while True:
        temperature = get_html(URL)
        store_temperature(temperature)
        time.sleep(5)
