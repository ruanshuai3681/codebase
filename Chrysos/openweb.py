import pandas as pd
from pathlib import Path
from datetime import datetime
import webbrowser
import threading
import time
import polars as pl

max_list = list(range(5, 25))
download_folder = Path(r"C:\Users\shuai.ruan\Downloads")
today = datetime.now().strftime("%Y%m%d")
date_name = str(today)

# Function to initiate downloads
def initiate_downloads():
    for i in max_list:
        addr = rf"https://max{i}:8000/qa/?&start=2024-01-01%2000:00:00&end=2024-04-06%2000:00:00&plot_type=ratio&x=acquisition_time&chrysos_certification=0&element=1&mad_thresh=3.5&exclude_superseded=True&show_plot=True&colour_by=1&crm_type=4&show_plot=False&download_csv=True&export_qa=csv"
        webbrowser.open(addr)
initiate_downloads()
