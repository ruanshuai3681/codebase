import os
import time
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser

def get_date_strings():
    today_with_dash = datetime.now().strftime("%Y-%m-%d")
    today_nodash = datetime.now().strftime("%Y%m%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y%m%d")
    return today_with_dash, today_nodash, yesterday, tomorrow

def get_max_unit():
    while True:
        max_unit = input("Which MAX unit do you want to check?\n")
        try:
            max_unit = int(max_unit)
            return max_unit
        except ValueError:
            print("Invalid input. Please enter an integer.")

def construct_url(max_unit):
    url = f"https://max{max_unit}:8000/qa/?&start=2024-01-01%2000:00:00&end=2024-04-06%2000:00:00&plot_type=ratio&x=acquisition_time&chrysos_certification=0&element=1&mad_thresh=3.5&exclude_superseded=True&show_plot=True&colour_by=1&crm_type=4&show_plot=False&download_csv=True&export_qa=csv"
    return url

def wait_for_download(today_nodash, yesterday, tomorrow):
    download_folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    download_folder = Path(download_folder_path)
    while True:
        downloaded_csv_files = list(download_folder.glob(f"{today_nodash}_*.csv")) + \
                           list(download_folder.glob(f"{yesterday}_*.csv")) + \
                           list(download_folder.glob(f"{tomorrow}_*.csv"))
        if len(downloaded_csv_files) == 0:
            print("Waiting for analysis...")
            time.sleep(3)
        else:
            return downloaded_csv_files[0]

def process_csv(csv_file_path, output_file_path):
    # Read CSV file into DataFrame, skipping the first row as it contains column names
    df = pd.read_csv(csv_file_path)
    # Convert the first column to pandas Timestamp object
    df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], format='%d/%m/%Y %H:%M:%S')
    # Convert the Timestamp objects to Unix timestamps
    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: x.timestamp())
    # Sort DataFrame by the first column (excluding the first row, which contains column names)
    df = df.iloc[1:].sort_values(by=df.columns[0], ascending=False)
    # Calculate time duration and shift by one position to align with the correct rows
    df['time duration'] = abs(df.iloc[:, 0].diff().fillna(pd.Timedelta(seconds=0)).shift(-1).fillna(0))/60
    # Reorder columns with "time duration" as the last column
    cols = list(df.columns)
    cols.remove('time duration')  # Remove "time duration" from the list
    cols.append('time duration')  # Append "time duration" to the end
    df = df[cols]  # Reorder columns

    # Write DataFrame to output CSV file
    df.to_csv(output_file_path, index=False)

def plot_histogram(df, max_unit, num_bins=120):
    last_column = df.iloc[:, -1]

    # Convert the column to numeric, ignoring any non-numeric values
    last_column_numeric = pd.to_numeric(last_column, errors='coerce')

    # Drop any NaN values resulting from non-numeric values
    last_column_numeric = last_column_numeric.dropna()

    # Filter out values higher than 180
    last_column_numeric_filtered = last_column_numeric[last_column_numeric <= 60]

    # Plot the histogram
    plt.hist(last_column_numeric_filtered, bins=num_bins, edgecolor='black')
    plt.xlabel('minutes')
    plt.ylabel('Frequency')
    plt.title(f'Time intervals of CRMs in Max{max_unit}')
    plt.show()

def main():
    _, today_nodash, tomorrow, _ = get_date_strings()
    max_unit = get_max_unit()
    url = construct_url(max_unit)
    webbrowser.open(url)
    csv_file_path = wait_for_download(today_nodash, tomorrow, tomorrow)
    output_file_path = Path(os.path.expanduser('~')) / 'Downloads' / f"MAX{max_unit}_CRM_duration_check.csv"
    process_csv(csv_file_path, output_file_path)
    df = pd.read_csv(output_file_path, header=None)
    plot_histogram(df, max_unit)

if __name__ == "__main__":
    main()
