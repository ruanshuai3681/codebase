import pandas as pd
import csv
savedpath= r"C:\Users\shuai.ruan\Downloads\20240105_QA_100ppm_20240105_132424 (1).csv"

df=pd.read_csv(savedpath)
print(df)

with open(savedpath, "r") as file1:
    content=file1.read()
    print(content)

with open(savedpath, "r") as file2:
    content2=csv.reader(file2)
    for raw in content2:
        print(raw)
#for keyward to iterate over the file and output as list
