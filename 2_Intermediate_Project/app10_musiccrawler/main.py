import requests
import selectorlib
from emailing import send_email
import time
import os.path
import sqlite3
import logging


URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

# db setting
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data.db")

with sqlite3.connect(db_path) as db:
    cursor = db.cursor()


def scraper(url):
    """Scrpae the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file(
        "2_Intermediate_Project/app10_musiccrawler/extract.yaml"
    )
    value = extractor.extract(source)["tours"]
    return value


def stored_extracted(extracted):
    row = extracted.split(",")
    row = [row.strip() for row in row]
    band, city, date = row
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    db.commit()


def read_extracted(extracted):
    row = extracted.split(",")
    row = [row.strip() for row in row]
    band, city, date = row
    cursor.execute(
        "SELECT * FROM events WHERE band=? AND city=? AND date =?", (band, city, date)
    )
    rows = cursor.fetchall()
    return rows


# def insert_to_db():


if __name__ == "__main__":
    while True:
        source = scraper(URL)
        extracted = extract(source)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read_extracted(extracted)
            if not row:
                stored_extracted(extracted)
                send_email(message=f"New event was found \n {extracted}")
        time.sleep(2)
