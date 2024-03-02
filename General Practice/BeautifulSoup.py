import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting image URLs
    images = soup.find_all('img')

    # Printing the image URLs
    for image in images:
        img_url = image['src']
        print(img_url)
else:
    print(f"Failed to fetch the content. Status Code: {response.status_code}")
