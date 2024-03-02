import webbrowser
from datetime import datetime, timedelta
from pathlib import Path

import polars as pl
from polars import read_csv

downloads = Path(r"C:\Users\shuai.ruan\Downloads")
output = Path.cwd().joinpath("trim_data")
output.mkdir(parents=True, exist_ok=True)

units = [f'max{i}' for i in range(1, 28)]


# Download or Process Files (rather than re-download each time)
download = False
today = datetime.now().strftime("%Y%m%d")
yesterday = (datetime.now()- timedelta(days=1)).strftime("%Y%m%d")
this_month = datetime.now().strftime("%Y%m")

if download:

    print("Cleaning up downloads file.")
    for file in downloads.glob(f"{today}_*Detector.csv"):
        print(f"Deleting {file}")
        file.unlink(missing_ok=True)

    for file in downloads.glob(f"{yesterday}_*Detector.csv"):
        print(f"Deleting {file}")
        file.unlink(missing_ok=True)

    for unit in units:  # ['max3']:#units:  # units:
        s = f"{unit}_{datetime.now()}"
        with open(downloads.joinpath(unit), 'w') as fid:
            fid.write(s)

        print(s)

        addr = rf"https://max{i}:8000/detector/?&start=2024-02-22%2000:00:00&end=2024-02-23%2000:00:00&x_type=acquisition_time&y_type=analysis_parameters__reference_trim__1&y_type=analysis_parameters__reference_trim__4&y_type=analysis_parameters__reference_trim__6&y_type=linac_energy_mev__value&y_type=linac_output__value&y_type=bromine_207_bot_rpd_gross__value&y_type=terbium_45_bot_rpd_gross__value&service_type=PAAU02&show_plot=False&download_csv=True&export_detector=csv"
        webbrowser.open(addr)


# Process All Data
else:
    missed_units = []

    averaged_results = []
    for unit in units:


        files = [f for f in downloads.glob(f"{today}*{unit.upper()}-*Detector.csv")]
        if not files:
            # Some units are living in the past
            files = [f for f in downloads.glob(f"{yesterday}*{unit.upper()}-*Detector.csv")]

        if files:
            #Only process one matching file
            file = files[0]
            print(f"Loading file {file}")
            df = read_csv(file, ignore_errors=True)
            print(f"{file} with {len(df)} rows and columns: {df.columns}")
            # print(f"Moving {file}")
            # move(file, output.joinpath(f"{unit}.csv"))

            averaged = df.group_by('Reference disc').mean().with_columns(unit=pl.lit(unit))
            averaged_results.append(averaged)


        else:
            print(f"Skipping {unit}")
            missed_units.append(unit)

        # Writing the progress out each time.
        df_avg = pl.concat(averaged_results, how="diagonal_relaxed")

        df_avg = df_avg.rename({k: k.lower().replace(" ", "_") for k in df_avg.columns})

        df_avg.write_csv(output.joinpath(f"{today}_trim_data.csv"))


    print(f"Missing: {missed_units}")
