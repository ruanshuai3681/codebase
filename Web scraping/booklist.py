from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

data = []
current_page = 1
proceed = True

while(proceed):
    print(f"current page: {current_page}")
    url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.title.text=="404 Not Found":
       proceed = False
    else:
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book in all_books:
            item = {}
            item["title"] = book.find("img").attrs["alt"]
            item["link"] = "https://books.toscrape.com/catalogue/" + book.find("a").attrs["href"]
            item["price"] = book.find("p", class_="price_color").text[2:]
            item["stock"] = book.find("p", class_="instock availability").text.strip()
            rating_element = book.find("p", class_=re.compile(r'star-rating'))
            if rating_element:
                item["rating"] = rating_element['class'][1]
            else:
                item["rating"] = None
            data.append(item)

    current_page += 49
df = pd.DataFrame(data)
df.to_csv(r"C:\Users\shuai.ruan\PycharmProjects\shuai_ruan\Web scraping\books.csv")
