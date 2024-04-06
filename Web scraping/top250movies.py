import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')
with open("IMDb Top 250 Movies.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
    print(soup)
