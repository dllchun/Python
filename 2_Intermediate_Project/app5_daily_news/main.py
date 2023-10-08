import requests as r

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
articles = content["articles"]

for article in articles:
    print(str(article["author"]) + "\n")
    print(str(article["description"]) + "\n")


# SMTP setup
