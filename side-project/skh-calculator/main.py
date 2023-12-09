from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time


class Bot(webdriver.Chrome):
    def __init__(
        self,
    ):
        pass

    def load_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognitos")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def load_first_page(self, page_number):
        # URL
        start_url = "https://www.cfs.gov.hk/tc_chi/nutrient/search1.php"
        self.get(start_url)
        while True:
            pass

    def create_csv(clear_list):
        header = [
            "食物類別",
            "食物細分類別",
            "食物名稱",
            "資料來源",
            "分量",
            "能量",
            "蛋白質",
            "碳水化合物",
            "脂肪",
            "膳食纖維",
            "糖",
            "飽和脂肪",
            "反式脂肪",
            "膽固醇",
            "鈣",
            "銅",
            "鐵",
            "鎂",
            "錳",
            "磷",
            "鉀",
            "鈉",
            "鋅",
            "維他命 C",
        ]

        df = pd.DataFrame(clear_list, columns=header)
        df.to_csv(
            "side-project/skh-calculator/test.csv",
            sep="\t",
            encoding="utf-8",
            index=False,
        )


def main():
    bot = Bot()
    for i in range(24):
        bot.load_first_page(i)


if __name__ == "__main__":
    main()
