import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import re
warnings.filterwarnings('ignore', message='Unverified HTTPS request')
url = "https://www.wsj.com/"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")
#h2_texts=soup.find_all("h2")[0].text.strip()
h2_texts = [h2.text.strip() for h2 in soup.find_all("h2")]
print(h2_texts)
