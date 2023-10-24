import glob2
import nltk
import ssl
from pathlib import Path

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_file():
    filepaths = glob2.glob(
        "/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app8_nlp_books/diary/*.txt"
    )
    return filepaths


def get_score():
    file_list = get_file()
    file_list = sorted(file_list)

    # NlTK
    analyzer = SentimentIntensityAnalyzer()

    positive_scores = []
    negative_scores = []
    date_list = []

    for file in file_list:
        with open(file, "r") as r:
            content = r.read()

            date = Path(file).stem
            date_list.append(date)
            date_list = sorted(date_list)

            # Sentiment Analysis
            result = analyzer.polarity_scores(content)
            print(result)
            pos = result["pos"]
            neg = result["neg"]
            positive_scores.append(pos)
            negative_scores.append(neg)

    return (
        positive_scores,
        negative_scores,
        date_list,
    )
    # print(positive_scores, negative_scores)


if __name__ == "__main__":
    get_score()
