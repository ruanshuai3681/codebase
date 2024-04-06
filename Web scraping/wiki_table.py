import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')
table=soup.find_all("table")[1]
table_head=table.find_all("th")
title_head_list=[title.text.strip() for title in table_head]
# or soup.find("table", class_="wikitable sortable")

df=pd.DataFrame(columns=title_head_list)

rows=table.find_all("tr")
for row in rows[1:]:
    row_data=row.find_all("td")
    individual_row_data=[data.text.strip() for data in row_data]
    length=len(df)
    df.loc[length] = individual_row_data

df.to_csv(r"C:\Users\shuai.ruan\PycharmProjects\shuai_ruan\Web scraping\wikidata.csv", index=False)
