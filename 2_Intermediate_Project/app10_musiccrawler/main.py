import requests
import selectorlib
from emailing import send_email
import time
import os.path
import sqlite3


URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


class Events:
    def scraper(self, url):
        """Scrpae the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file(
            "2_Intermediate_Project/app10_musiccrawler/extract.yaml"
        )
        value = extractor.extract(source)["tours"]
        return value


class Database:
    def __init__(self, database_path):
        print("Database Connected")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, database_path)

        self.connection = sqlite3.connect(db_path)
        print(self.connection)

    def stored(self, extracted):
        row = extracted.split(",")
        row = [row.strip() for row in row]
        band, city, date = row
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()

    def read(self, extracted):
        row = extracted.split(",")
        row = [row.strip() for row in row]
        band, city, date = row
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "SELECT * FROM events WHERE band=? AND city=? AND date =?",
            (band, city, date),
        )
        rows = self.cursor.fetchall()
        return rows


if __name__ == "__main__":
    while True:
        event = Events()
        source = event.scraper(URL)
        extracted = event.extract(source)
        print(extracted)

        if extracted != "No upcoming tours":
            database = Database(database_path="data.db")
            row = database.read(extracted)
            if not row:
                database.stored(extracted)
                send_email(message=f"New event was found \n {extracted}")
        time.sleep(2)
