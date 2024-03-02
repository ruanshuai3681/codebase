import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract data using BeautifulSoup
    # ...

# Continue processing the extracted data

