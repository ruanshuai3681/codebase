import os
import time
from datetime import datetime, timedelta
from pathlib import Path
import webbrowser
import pandas as pd
from tabulate import tabulate

def get_date_strings():
    today_with_dash = datetime.now().strftime("%Y-%m-%d")
    today_nodash = datetime.now().strftime("%Y%m%d")
    last_week_date_with_dash = (datetime.now() - timedelta(weeks=1)).strftime("%Y-%m-%d")
    last_week_date_nodash = (datetime.now() - timedelta(weeks=1)).strftime("%Y%m%d")
    return today_with_dash, today_nodash, last_week_date_with_dash, last_week_date_nodash

def get_max_unit():
    while True:
        max_unit = input("Which MAX unit do you want to check?\n")
        try:
            max_unit = int(max_unit)
            return max_unit
        except ValueError:
            print("Invalid input. Please enter an integer.")

def construct_url(max_unit, today_with_dash, last_week_date_with_dash):
    url = f"https://max{max_unit}:8000/detector/?"
    url += f"&start={last_week_date_with_dash}%2000:00:00"
    url += f"&end={today_with_dash}%2000:00:00&x_type=acquisition_time"
    url += "&y_type=linac_energy_mev__value&y_type=linac_output__value"
    url += "&y_type=beam_position_mm__gold__value&y_type=calibration_beam_position_mm"
    url += "&y_type=bromine__ideal_zero_mass_ratio__value&y_type=bromine__zero_mass_ratio"
    url += "&y_type=data_quality__low_energy_noise_bot_cps__value&y_type=data_quality__low_energy_noise_top_cps__value"
    url += "&y_type=terbium_299_bot_counts__value"
    url += "&y_type=scandium_889_bot_counts__value"
    url += "&y_type=iridium_316_bot_counts__value"
    url += "&y_type=hafnium_214_bot_counts__value"
    url += "&y_type=bromine_207_bot_fwhm_kev__value&y_type=bromine_207_top_fwhm_kev__value"
    url += "&service_type=K-Cal%20PAAU02&show_plot=False&download_csv=True&export_detector=csv"
    return url

def wait_for_download(today_nodash):
    download_folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    download_folder = Path(download_folder_path)
    while True:
        downloaded_csv_files = list(download_folder.glob(f"{today_nodash}_*.csv"))
        if len(downloaded_csv_files) == 0:
            print("Waiting for analysis...")
            time.sleep(3)
        else:
            return downloaded_csv_files[0]

def process_csv(csv_file_path):
    df = pd.read_csv(csv_file_path)
    selected_columns = df.iloc[:, 11:24]
    average_values = selected_columns.mean().to_frame().T
    df = pd.concat([df, average_values], ignore_index=True)
    df = df[selected_columns.columns]
    df = df.tail(1).T
    return df

def save_last_row(df, output_file_path):
    df.to_csv(output_file_path, header=False)
    print(f"Analysis completed! \nMonthly check data saved in {output_file_path}")

def print_csv_content(csv_file_path):
    df = pd.read_csv(csv_file_path, header=None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', None)
    print("Averaged data over the past week from KCAL:")
    print(tabulate(df, headers='keys', tablefmt='grid'))

def delete_csv(csv_file_path):
    os.remove(csv_file_path)

def main():
    today_with_dash, today_nodash, last_week_date_with_dash, _ = get_date_strings()
    max_unit = get_max_unit()
    url = construct_url(max_unit, today_with_dash, last_week_date_with_dash)
    webbrowser.open(url)
    csv_file_path = wait_for_download(today_nodash)
    last_row_transposed = process_csv(csv_file_path)
    output_file_path = Path(os.path.expanduser('~')) / 'Downloads' / f"MAX{max_unit} monthly check data.csv"
    save_last_row(last_row_transposed, output_file_path)
    print_csv_content(output_file_path)
    delete_csv(csv_file_path)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
