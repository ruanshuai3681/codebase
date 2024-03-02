import requests
from bs4 import BeautifulSoup
url = "https://www.abc.net.au/news"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')


paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)
