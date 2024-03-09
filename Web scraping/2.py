from bs4 import BeautifulSoup
import requests

#the website URL
url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

#Send a GET request to the URL
response = requests.get(url_link, verify=False)

#Extract the text content of the response
result = response.text

doc = BeautifulSoup(result, "html.parser")

print(doc.prettify())
