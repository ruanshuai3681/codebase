import pandas as pd
data = {"height":[1, 2, 3], "width":[2,3,1]}
df=pd.DataFrame(data)
print(data)
print("-------------")
df1=df[df.height>df.width]
df2=df.query("height<width")

print(df1)
print("-------------")
print(df2)

df["depth"] = [7,8,9] #add a new column
df["4D"]=[6,None, 7]
print("-------------")
print(df)

filtered_data=df[df["depth"]>8]
print(filtered_data)

mean_depth=df["depth"].mean()
print(mean_depth)

df=df.fillna(0)# Fill missing values with a specific value
print(df)

df=df.dropna()# Drop rows with missing values
print(df)

df.query("width>@df.width.mean()")
df[(df.height >2) & (df.width > 3)]
df.query("height >2 & width > 3")
df.query('height>2 | width >3', inplace=True) #or
print(df)
