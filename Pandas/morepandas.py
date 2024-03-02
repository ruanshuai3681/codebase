import pandas as pd
data={"raw":[1,2,3], "double-raw":[2,4,6]}
df=pd.DataFrame(data)

print(data)
print("-------------------")
print(df.astype(float).dtypes) #convert types #check types
print(df.raw.astype(int))
print(df.dtypes)
