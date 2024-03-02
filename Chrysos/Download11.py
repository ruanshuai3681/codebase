import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
import webbrowser
import threading
import time
import polars as pl
import os

max_list = list(range(1, 30))
today_with_dash = datetime.now().strftime("%Y-%m-%d")
today_nodash = datetime.now().strftime("%Y%m%d")
last_4week_date_with_dash = (datetime.now() - timedelta(weeks=12)).strftime("%Y-%m-%d")
last_4week_date_nodash = (datetime.now() - timedelta(weeks=12)).strftime("%Y%m%d")

download_folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')
download_folder = Path(download_folder_path)
downloaded_csv_files = list(download_folder.glob(f"20240228_*.csv"))

for i in max_list:
    url = f"https://max{i}:8000/detector/?"
    url += f"&start={last_4week_date_with_dash}%2000:00:00"
    url += f"&end=2024-02-28%2000:00:00&x_type=acquisition_time"
    url += "&y_type=gold_279_bot_counts__value&y_type=gold_279_top_counts__value"
    url += "&crm_list=OREAS__234&crm_list=OREAS__242&crm_list=OREAS__247"
    url += "&y_type=net_mass_g"
    url += "&service_type=PAAU02&show_plot=False&download_csv=True&export_detector=csv"
    webbrowser.open(url)

def wait_for_download(today_nodash):
    while True:
        downloaded_csv_files = list(download_folder.glob(f"20240228_*.csv"))
        if len(downloaded_csv_files) == 1:
            print("Waiting for analysis...")
            time.sleep(3)
        else:
            return downloaded_csv_files[0]

for filename in os.listdir(download_folder):
    if filename.startswith(f"20240228_"):
        filepath = os.path.join(download_folder, filename)

        # Read the CSV file into a DataFrame
        df = pd.read_csv(filepath)

        # Add a new column with the filename
        df['Filename'] = filename

        # Write the DataFrame back to the CSV file
        df.to_csv(filepath, index=False)
