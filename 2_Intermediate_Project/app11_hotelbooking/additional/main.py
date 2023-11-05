import pandas as pd
from fpdf import FPDF


"""
- Classes 
    - Article 
    
- Functions
    - User can view all article information
    - User can buy one of the article
    - After puchased the article, will receive an invoice
"""

df = pd.read_csv(
    "2_Intermediate_Project/app11_hotelbooking/additional/articles.csv",
    dtype={"id": str, "in stock": int},
)

df.index += 1


class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.article_name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.article_price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def buy(self):
        df.loc[df["id"] == self.article_id, "in stock"] -= 1
        df.to_csv(
            "2_Intermediate_Project/app11_hotelbooking/additional/articles.csv",
            index=False,
        )

    def available(self):
        availability = df.loc[df["id"] == self.article_id, "in stock"].squeeze()
        if availability > 0:
            return True
        else:
            return False

    def generate_invoice(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style="b")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.101", border=0, ln=1, align="l")
        pdf.set_font(family="Times", size=16, style="b")
        pdf.cell(
            w=50, h=8, txt=f"Article: {self.article_name}", border=0, ln=1, align="l"
        )
        pdf.set_font(family="Times", size=16, style="b")
        pdf.cell(
            w=50, h=8, txt=f"Price: {self.article_price}", border=0, ln=1, align="l"
        )

        pdf.output(f"2_Intermediate_Project/app11_hotelbooking/additional/1.pdf")


if __name__ == "__main__":
    print(df)
    article_id = input("Choose an article to buy: ")
    article = Article(article_id)
    if article.available():
        article.buy()
        article.generate_invoice()

    else:
        print("this article is out of stock")
