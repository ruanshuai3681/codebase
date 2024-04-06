import requests
from bs4 import BeautifulSoup
import warnings

page_url = "https://max14:8000/admin/photon_assay/crmjar/16/change/?_changelist_filters=p%3D17"
page_response = requests.get(page_url, verify=False)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

    # Parse the response with Beautiful Soup
soup1 = BeautifulSoup(page_response.text, 'html.parser')

    # Now you can work with the parsed HTML as needed
    # For example, extract data or perform further actions
print(soup1.prettify())  # Print the prettified HTML for demonstration


if login_response.status_code == 200:
    # If successful, you are now logged in and can access authenticated pages
    page_url = "https://max14:8000/admin/photon_assay/crmjar/16/change/?_changelist_filters=p%3D17"
    page_response = session.get(page_url, verify=False)

    # Parse the page using BeautifulSoup
    if page_response.status_code == 200:
        page_soup = BeautifulSoup(page_response.content, 'html.parser')
        print(page_soup)
    else:
        print("Failed to fetch page")
else:
    print("Login failed")


