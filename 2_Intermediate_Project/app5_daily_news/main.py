import requests as r
from send_email import send_email

# API info
with open("2_Intermediate_Project/app5_daily_news/api_key.txt", "r") as f:
    api_key = f.read()
    f.close()

url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-09-08&sortBy=publishedAt&apiKey={api_key}"


# Make request
request = r.get(url)

# Get a dictionary with data
content = request.json()

# Access the title and description

body = ""
for article in content["articles"]:
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
