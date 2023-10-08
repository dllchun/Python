import requests as r
from send_email import send_email

# API info
with open("2_Intermediate_Project/app5_daily_news/api_key.txt", "r") as f:
    api_key = f.read()
    f.close()

# Parameters

date = "2023-10-01"
language = "en"
page_size = 50

url = f"https://newsapi.org/v2/everything?q=tesla&from={date}&sortBy=publishedAt&apiKey={api_key}&language={language}"


# Make request
request = r.get(url)

# Get a dictionary with data
content = request.json()

# Access the title and description

body = "Subject: Today's news"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = (
            body
            + article["title"]
            + "\n"
            + article["description"]
            + "\n"
            + article["url"]
            + 2 * "\n"
        )


body = body.encode("utf-8")

send_email(body)
