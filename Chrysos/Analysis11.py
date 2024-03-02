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
downloaded_csv_files = list(download_folder.glob("20240228_*.csv")) + list(download_folder.glob("20240229_*.csv"))

for filename in os.listdir(download_folder):

    if filename.startswith("20240228_") or filename.startswith("20240229_"):
        filepath = os.path.join(download_folder, filename)

        # Read the CSV file into a DataFrame
        df = pd.read_csv(filepath)

        # Add a new column with the filename
        df['Filename'] = filename

        # Write the DataFrame back to the CSV file
        df.to_csv(filepath, index=False)

def execute_commands(download_folder, downloaded_csv_files):
    columns = []
    column_names = ["Filename", "Sample id", "Gold 279 bot counts  value", "Gold 279 top counts  value", "Net mass g"]
    for csv_file in downloaded_csv_files:
        df = pd.read_csv(csv_file)
        selected_columns = df[column_names]
        columns.append(selected_columns)
    combined_df = pd.concat(columns, axis=0)
    output_file_path = download_folder / "combined_output.csv"
    combined_df.to_csv(output_file_path, index=False)

    #for file in downloaded_csv_files:
       # file.unlink()


execute_commands(download_folder, downloaded_csv_files)
