import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.exceptions import ConnectTimeout

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
    try:
        response = session.get(login_url, verify=False, timeout=10)  # Timeout set to 10 seconds
    except ConnectTimeout as e:
        print(f"Connection to max{max_unit} timed out.")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    login_data = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrf_token,
    }
    headers = {'Referer': login_url}
    try:
        login_response = session.post(login_url, data=login_data, headers=headers, timeout=10)  # Timeout set to 10 seconds
    except ConnectTimeout as e:
        print(f"Connection to max{max_unit} timed out.")
        return None

    return session

def scrape_crm_data(session, max_unit):
    """Scrape CRM data"""
    page_list = list(range(0, 51))
    df = pd.DataFrame(columns=['jar_barcode'])  # Initialize DataFrame
    for i in page_list:
        page_url = f"https://max{max_unit}:8000/admin/photon_assay/jar/?p={i}"
        try:
            page_response = session.get(page_url, verify=False, timeout=10)  # Timeout set to 10 seconds
        except ConnectTimeout as e:
            print(f"Connection to max{max_unit} timed out.")
            return None
        page_soup = BeautifulSoup(page_response.content, 'html.parser')
        all_barcode = page_soup.find_all('td', class_="field-jar_barcode")
        jar_list = [jar_barcode.text.strip() for jar_barcode in all_barcode]
        for barcode in jar_list:
            df = df._append({'jar_barcode': barcode}, ignore_index=True)
    return df  # Return DataFrame

def main():
    # Initialize an empty DataFrame to store the results
    final_df = pd.DataFrame(columns=['MAX Unit', 'CRM_number', 'Client_jar_number', 'CRM_number_for_every_100_Client_jars'])

    for max_unit in range(0, 33):
        username = 'shuai.ruan'
        password = 'Laichesin@3681'
        session = login_to_website(max_unit, username, password)
        if session is None:
            print(f"Failed to login to MAX unit {max_unit}. Skipping...")
            continue

        df = scrape_crm_data(session, max_unit)
        if df is None:
            print(f"Failed to scrape CRM data from MAX unit {max_unit}. Skipping...")
            continue

        # Count rows containing and not containing "CRM"
        contains_crm = 0
        does_not_contain_crm = 0
        for index, row in df.iterrows():
            if "CRM" in row['jar_barcode']:
                contains_crm += 1
            else:
                does_not_contain_crm += 1

        # Calculate CRM to Client jar ratio
        ratio = 100 * contains_crm / does_not_contain_crm if does_not_contain_crm != 0 else 0

        # Append results to the final DataFrame
        final_df = final_df._append({
            'MAX Unit': max_unit,
            'CRM_number': contains_crm,
            'Client_jar_number': does_not_contain_crm,
            'CRM_number_for_every_100_Client_jars': ratio
        }, ignore_index=True)

    # Save the final DataFrame to the same CSV file
    final_df.to_csv(rf"C:\Users\shuai.ruan\PycharmProjects\shuai_ruan\Web scraping\CRM_Counts_All_Max.csv", index=False)

if __name__ == "__main__":
    main()
