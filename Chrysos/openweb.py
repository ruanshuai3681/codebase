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
def initiate_downloads():
    for i in max_list:
        addr = rf"https://max{i}:8000/detector/?&start=2024-03-11%2000:00:00&end=2024-03-12%2000:00:00&x_type=acquisition_time&y_type=bromine__ideal_zero_mass_ratio__value&y_type=bromine__zero_mass_ratio&show_plot=True&colour_by=6"
        webbrowser.open(addr)
initiate_downloads()
