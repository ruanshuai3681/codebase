import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

url = "https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

df = pd.DataFrame(columns=["title", "rank", "year"])  # Create an empty DataFrame with a single "title" column

movies = soup.find_all("article", class_="PreviewCard__Article-sc-7y1ad6-0 gUNVnM")
for movie in movies:
    title = movie.find_all("h1")  # Extract the title of the movie
    rank = movie.find_all("p", class_="ResultsPage__Rank-sc-of10co-1 gsVRkZ PreviewCard__label")  # Extract the title of the movie
    year = movie.find_all("p", class_="ResultsPage__P-sc-of10co-2 eUEyPc")
    individual_rank = [data.text.strip("[]=").replace("'", "") for data in rank]
    individual_title = [data.text.strip("[]").replace("'", "") for data in title]
    individual_year = [data.text.strip("[]").replace("'", "") for data in year]
    length=len(df)
    df.loc[length] = [individual_title, individual_rank, individual_year]

print(df)
df.to_csv(r"C:\Users\shuai.ruan\PycharmProjects\shuai_ruan\Web scraping\movies.csv")
