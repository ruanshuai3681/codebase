import os.path

import numpy as np
import pandas as pd

# file_path = r"C:\Users\aiden.chrisan\Downloads\20240201_144833_FAT1-NTCI1_Detector.csv"

try:
    print(
        'You will be asked to input the path to a CSV. '
        'This CSV should have been downloaded from the FAT unit with the Primary and Secondary gross RPDs.'
        'The trim factors should also be included.')
    file_path = input("Enter the path of the Excel file: ")
    file_path = file_path.strip('"')
    file_path = rf"{file_path}"
    df = pd.read_csv(file_path)
    print("Successfully loaded the Excel file.")
except FileNotFoundError:
    print(f"Error: The file at '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The Excel file at '{file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: Unable to parse the Excel file at '{file_path}'. Check if it's a valid Excel file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

disc_family = input('Input disc family name that you are interested in trimming (state either AX or CX): ')
if disc_family == 'CX':
    try:
        cxc_columns = ['Reference disc', 'Germanium 140 bot rpd gross  value', 'Terbium 45 bot rpd gross  value',
                       'Analysis parameters  reference trim  2', 'Analysis parameters  reference trim  6']
        # Ref trim 2 is Ge, Ref trim 6 is Tb

        cxc_df = df[cxc_columns]
        # print(cxc_df)

        cxc_rpd_df = cxc_df.groupby('Reference disc').mean()

        ge_average_rpd_gross = cxc_rpd_df['Germanium 140 bot rpd gross  value'].mean()
        tb_average_rpd_gross = cxc_rpd_df['Terbium 45 bot rpd gross  value'].mean()

        cxc_primary_trims_df = cxc_rpd_df[
                                   'Germanium 140 bot rpd gross  value'] / ge_average_rpd_gross
        cxc_secondary_trims_df = cxc_rpd_df[
                                     'Terbium 45 bot rpd gross  value'] / tb_average_rpd_gross
        cxc_trims_df = pd.merge(cxc_primary_trims_df, cxc_secondary_trims_df, on='Reference disc')
        print(cxc_trims_df)
        print(
            'Note: if the original disc trims are NOT 1 then you will need to divide these trims by the current reference trim')

    except Exception as e:
        print(f"Data in CSV may not exist. Consider checking which disc type is to be trimmed: {e}")

elif disc_family == 'AX':
    try:
        axc_columns = ['Reference disc', 'Bromine 207 bot rpd gross  value', 'Terbium 45 bot rpd gross  value']
        axc_df = df[axc_columns]

        axc_rpd_df = axc_df.groupby('Reference disc').mean()

        br_average_rpd_gross = axc_rpd_df['Bromine 207 bot rpd gross  value'].mean()
        tb_average_rpd_gross = axc_rpd_df['Terbium 45 bot rpd gross  value'].mean()

        axc_primary_trims_df = axc_rpd_df[
                                   'Bromine 207 bot rpd gross  value'] / br_average_rpd_gross
        axc_secondary_trims_df = axc_rpd_df[
                                     'Terbium 45 bot rpd gross  value'] / tb_average_rpd_gross
        axc_trims_df = pd.merge(axc_primary_trims_df, axc_secondary_trims_df, on='Reference disc')
        print(axc_trims_df)

    except Exception as e:
        print(f"Data in CSV may not exist. Consider checking which disc type is to be trimmed: {e}")

else:
    print('Code exited')
