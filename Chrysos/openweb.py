import pandas as pd
from pathlib import Path
from datetime import datetime
import webbrowser
import threading
import time
import polars as pl

max_list = list(range(1, 25))
download_folder = Path(r"C:\Users\shuai.ruan\Downloads")
today = datetime.now().strftime("%Y%m%d")
date_name = str(today)

# Function to initiate downloads
def initiate_downloads():
    for i in max_list:
        addr = rf"https://max{i}:8000/config/reference/slots/"
        webbrowser.open(addr)
initiate_downloads()
