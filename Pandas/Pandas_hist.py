import pandas as pd
import matplotlib.pyplot as plt

file_path=r"C:\Users\shuai.ruan\Downloads\20240105_QA_50ppm_20240105_100227 (1).csv"
df=pd.read_csv(file_path)

plt.figure()
plt.hist(df["result_value"], bins=220, label="data")
plt.legend()
plt.show()
