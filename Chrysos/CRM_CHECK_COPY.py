import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_max_unit():
    """Prompt user to input MAX unit number"""
    while True:
        max_unit = input("Which MAX unit do you want to check?\n")
        try:
            max_unit = int(max_unit)
            return max_unit
        except ValueError:
            print("Invalid input. Please enter an integer.")

def login_to_website(max_unit, username, password):
    """Login to the website"""
    login_url = f'https://max{max_unit}:8000/admin/login/?next=/admin/'
    session = requests.Session()
    response = session.get(login_url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    login_data = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrf_token,
    }
    headers = {'Referer': login_url}
    login_response = session.post(login_url, data=login_data, headers=headers)
    return session

def scrape_crm_data(session, max_unit):
    """Scrape CRM data"""
    df = pd.DataFrame(columns=["jar_barcode", "CRM_type", "gross_mass", "fill", "date"])
    crm_list = list(range(1711, 700, -1))
    for i in crm_list:
        page_url = f"https://max{max_unit}:8000/admin/photon_assay/crmjar/{i}/change/"
        page_response = session.get(page_url, verify=False)
        page_soup = BeautifulSoup(page_response.content, 'html.parser')
        retired = page_soup.find('input', attrs={'name': 'retired'})
        date_url = f"https://max{max_unit}:8000/admin/photon_assay/crmjar/{i}/history/"
        date_response = session.get(date_url, verify=False)
        date_soup = BeautifulSoup(date_response.content, 'html.parser')
        try:
            jar_barcode = page_soup.find('input', attrs={'name': 'jar_barcode'}).get('value')
            jar_CRM = page_soup.find('input', attrs={'name': 'standard_id'}).get('value')
            jar_gross_mass = page_soup.find('input', attrs={'name': 'gross_mass_g'}).get('value')
            jar_fill = page_soup.find('input', attrs={'name': 'fill_pc'}).get('value')
            jar_date = date_soup.find_all("th", attrs={'scope': 'row'})[-1]
            jar_date_individual = jar_date.text.strip()
            retired_str = str(retired)
            if 'checked' in retired_str:
                df = df._append({"jar_barcode": jar_barcode, "CRM_type": jar_CRM, "gross_mass": jar_gross_mass, "fill": jar_fill, "date": jar_date_individual}, ignore_index=True)
        except AttributeError:
            continue
    return df

def main():
    max_unit = get_max_unit()
    username = 'shuai.ruan'
    password = 'Laichesin@3681'
    session = login_to_website(max_unit, username, password)
    df = scrape_crm_data(session, max_unit)
    print(df)
    df.to_csv(rf"C:\Users\shuai.ruan\PycharmProjects\shuai_ruan\Web scraping\retired_CRM_Max{max_unit}.csv")

if __name__ == "__main__":
    main()
