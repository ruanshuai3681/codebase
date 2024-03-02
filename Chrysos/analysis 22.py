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
last_4week_date_with_dash = (datetime.now() - timedelta(weeks=4)).strftime("%Y-%m-%d")
last_4week_date_nodash = (datetime.now() - timedelta(weeks=4)).strftime("%Y%m%d")


download_folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')
download_folder = Path(download_folder_path)
downloaded_csv_files = list(download_folder.glob(f"{today_nodash}_*.csv"))

df = pd.read_csv(r"C:\Users\shuai.ruan\Downloads\combined_output.csv")
df['Max_unit'] = df['Filename'].str.extract(r'MAX(\d+)-')
#df['CRM_Jar'] = df['Sample id'].str.split('_').str[1]
df['CRM_Jar'] = df['Sample id'].str[-3:]
df['Gold 279 bot counts  value per gram'] = df['Gold 279 bot counts  value']/df["Net mass g"]
df['Gold 279 top counts  value per gram'] = df['Gold 279 top counts  value']/df["Net mass g"]
df.to_csv(r"C:\Users\shuai.ruan\Downloads\combined_output.csv", index=False)

#grouped = df.groupby(['Max_Unit', "Sample id"])
#mean_data = grouped[["Gold 279 bot counts  value", "Gold  signal per net mass g  value", "Gold 279 top counts  value", "Net mass g"]].mean().reset_index()
#output_file_path = download_folder / "ave_combined_output.csv"
#mean_data.to_csv(output_file_path, index=False)

