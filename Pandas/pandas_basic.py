import pandas as pd
gold_data=r"C:\Users\shuai.ruan\PycharmProjects\shuai ruan\Chrysos\20240105_QA_100ppm_20240105_132424 (2).csv"
df=pd.read_csv(gold_data)
df1=pd.read_csv(gold_data)
df2=pd.read_csv(gold_data, usecols=["jar_barcode", 'result_value',"result_sd"])#select columns
df3=pd.read_csv(gold_data, skiprows=1, skipfooter=1, thousands=",")# index_col="jar_barcode", use this column as index
# or df.index="jar_barcode"
print(df2.tail(1).to_json())
print(df2.tail(1))
print(df2.head(1))
print(df1.columns)
print(df1.dtypes)
print(df1[["jar_barcode", 'result_value']].head(1))#show selected columns
print(df1.at[0, "jar_barcode"]) #single datapoint
print(df1.loc[0:2, "jar_barcode":"result_sd"])#show selected rows and columns
print(df3.loc[0:3])#show selected rows
print(df1.info())
print(df1.jar_barcode.value_counts())
df1.rename(columns={"sample_id":"SAMPLE_ID"}, inplace=True)#rename column
df4=df1.rename(columns={"fill_pc":"FILL-_PC"})#rename column
df5=df1.rename({"fill_pc":"FILLll-_PC"}, axis=1)#rename column axis=0 is row, axis=1 is column
df55=df1.rename(index={1:1111}).drop(index=1111)
df6=df.drop([0,1,2]) #delete rows
df7=df.drop(["jar_barcode", "sample_id"], axis=1) #delete columns axis=0 is row, axis=1 is column
df8=df.drop(index=[0,1], columns=["jar_barcode", "sample_id"])#delete columns and rows
print(df4.loc[0])
print(df5.loc[0])
print(df1.loc[0])
print("------------")
print(df6)
print(df7)
print(df55.loc[0:3])
df5.to_csv("modified_20240105_QA_100ppm_20240105_132424 (2).csv", index=False)
df5.to_excel("modified_20240105_QA_100ppm_20240105_132424 (2).xlsx", index=False)
print("------------")
df = df.dropna(thresh=2)# Drop rows with at least two missing values
df9 = df.dropna(axis=1)# Drop columns with any missing values
df10=df.dropna(subset=["jar_barcode", "sample_id"])# Drop rows with any missing values in such columns
df.dropna(subset=["jar_barcode", "sample_id"], how="all")# Drop rows only with both missing values in such columns
df.isna()
df.isna().sum()
df.dropna(axis=1, how="all", inplace=True) #delete rows that have no value
df[df.duplicated((keep=False))] =show both rows that are duplicated, #drop the duplicated rows have the same columns data
df.drop_duplicates()
#df.drop_duplicates(subset="", keep="last") onlky keep the last shwon data 】
#df = df[df['column_name'] != 'value_to_exclude'].drop(columns=['column_name1', 'column_name2'])
print(df9)
print(df10)
