import requests
import selectorlib
from emailing import send_email
import time


URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


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


def store(extracted):
    with open("2_Intermediate_Project/app10_musiccrawler/data.txt", "a") as file:
        file.write(extracted + "\n")


def read(extracted):
    with open("2_Intermediate_Project/app10_musiccrawler/data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    while True:
        scraped = scraper(URL)
        extracted = extract(scraped)
        print(extracted)

        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(message=f"Hey new event was found! \n {extracted}")

        time.sleep(10)
