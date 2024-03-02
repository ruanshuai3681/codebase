import pandas as pd
from pathlib import Path
from datetime import datetime
import webbrowser
import threading
import time
import polars as pl

max_list = list(range(1, 28))
download_folder = Path(r"C:\Users\shuai.ruan\Downloads")
today = datetime.now().strftime("%Y%m%d")
date_name = str(today)

# Function to initiate downloads
def initiate_downloads(max_list):
    for i in max_list:
        addr = rf"https://max{i}:8000/detector/?&start=2024-02-22%2000:00:00&end=2024-02-23%2000:00:00&x_type=acquisition_time&y_type=linac_energy_mev__value&y_type=terbium_45_bot_rpd_gross__value&service_type=PAAU02&show_plot=False&download_csv=True&export_detector=csv"
        webbrowser.open(addr)

# Function to check if all CSV files are downloaded
def all_files_downloaded(download_folder, date_name):
    downloaded_csv_files = list(download_folder.glob(f"{date_name}_*.csv"))
    return len(downloaded_csv_files) == len(max_list), downloaded_csv_files

# Function to execute commands after downloads are completed
def execute_commands(download_folder, downloaded_csv_files):
    columns = []
    column_names = ["Reference disc", "Linac energy mev  value", "Terbium 45 bot rpd gross  value", "Linac energy mev  sd"]
    for csv_file in downloaded_csv_files:
        df = pd.read_csv(csv_file)
        selected_columns = df[column_names]
        columns.append(selected_columns)
    combined_df = pd.concat(columns, axis=0)
    output_file_path = download_folder / "combined_output.csv"
    combined_df.to_csv(output_file_path, index=False)

    for file in downloaded_csv_files:
        file.unlink()

    print(f"Combined data saved to {output_file_path}")

    # Calculate mean grouped by 'Reference disc' after combining CSVs
    data = pd.read_csv(output_file_path)
    mean_data = data.groupby('Reference disc').mean().reset_index()
    output_file_path = download_folder / "ave_combined_output.csv"
    mean_data.to_csv(output_file_path, index=False)

# Function to monitor downloads and execute commands
def monitor_downloads(download_folder, date_name):
    while True:
        all_downloaded, downloaded_csv_files = all_files_downloaded(download_folder, date_name)
        if all_downloaded:
            execute_commands(download_folder, downloaded_csv_files)
            break
        time.sleep(1)  # Adjust the sleep time as needed to reduce CPU usage



# Initiate downloads in a separate thread
download_thread = threading.Thread(target=initiate_downloads, args=(max_list,))
download_thread.start()

# Monitor downloads and execute commands in a separate thread
process_thread = threading.Thread(target=monitor_downloads, args=(download_folder, date_name))
process_thread.start()

# Continue with other tasks while downloads and processing are in progress
print("Waiting for all CSV files to be downloaded...")

# Wait for both threads to complete before exiting the script
download_thread.join()
process_thread.join()
