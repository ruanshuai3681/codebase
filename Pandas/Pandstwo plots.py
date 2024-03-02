import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=r"C:\Users\shuai.ruan\Downloads\20240105_QA_100ppm_20240105_132424 (2).csv"
df=pd.read_csv(data)
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(df["list"],df["gross_mass_g"], color="blue", label="gross mass")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.title("jar mass")
plt.legend()

plt.subplot(1,2,2)
plt.scatter(df["list"], df["result_value"], color="red", label="conentration")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.title("jar gold concentration")
plt.legend()

#print(df.loc[0])
plt.tight_layout()
print(df.sort_values(by="result_value"))
#print(df.describe())
#plt.show()
