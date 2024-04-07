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
    url = f"https://max{max_unit}:8000/qa/?&start=2024-04-04%2000:00:00&end=2024-04-06%2000:00:00&plot_type=ratio&x=acquisition_time&chrysos_certification=0&element=1&mad_thresh=3.5&exclude_superseded=True&show_plot=True&colour_by=1&crm_type=4&show_plot=False&download_csv=True&export_qa=csv"
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

def plot_histograms(all_results, num_bins=60):
    num_columns = len(all_results.columns)
    num_rows = (num_columns + 1) // 2  # Calculate the number of rows for subplots

    fig, axs = plt.subplots(num_rows, 2, figsize=(12, 6 * num_rows))
    axs = axs.flatten()

    for i, column in enumerate(all_results.columns):
        data = all_results[column]
        ax = axs[i]
        ax.hist(data, bins=num_bins, edgecolor='black')
        ax.set_xlabel('minutes')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Time intervals of CRMs in {column}')

    # Hide any remaining subplots
    for j in range(num_columns, num_rows * 2):
        axs[j].axis('off')

    plt.tight_layout()
    plt.savefig('all_histograms.png')
    plt.show()

def main():
    _, today_nodash, tomorrow, _ = get_date_strings()

    # Create an empty DataFrame to store results for all max units
    all_results = pd.DataFrame()

    # Iterate over all max units from 1 to 32
    for max_unit in range(1, 4):
        try:
            url = construct_url(max_unit)
            webbrowser.open(url)

            csv_file_path = wait_for_download(today_nodash, tomorrow, tomorrow)
            output_file_path = Path(os.path.expanduser('~')) / 'Downloads' / f"MAX{max_unit}_CRM_duration_check.csv"
            process_csv(csv_file_path, output_file_path)

            # Read the processed CSV data
            df = pd.read_csv(output_file_path, header=None)

            # Extract the last column
            last_column = df.iloc[:, -1]

            # Add a column for max unit to the DataFrame with corresponding max unit title
            last_column.name = f'Max{max_unit} - {construct_url(max_unit)}'

            # Concatenate the last column to the all_results DataFrame
            all_results = pd.concat([all_results, last_column], axis=1)
        except Exception as e:
            print(f"Error processing Max{max_unit}: {e}")

    # Save all results to one CSV file
    output_file_path2 = Path(os.path.expanduser('~')) / 'Downloads' / f"ALL_MAX_unit_CRM_duration_check.csv"
    all_results.to_csv(output_file_path2, header=None)
    plot_histograms(all_results)

if __name__ == "__main__":
    main()
