from bs4 import BeautifulSoup
import requests

# Send a GET request to the webpage
response = requests.get('https://www.bbc.com/news', verify=False)

soup = BeautifulSoup(response.text, 'html.parser')
# Example: Extracting the title of the webpage

title = soup.title.text
print('Page Title:', title)

heading = soup.find('h1')
print('Main Heading:', heading.text)

paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)

