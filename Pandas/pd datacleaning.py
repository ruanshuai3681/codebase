new_df = df.dropna(inplace=True) #delete the row, it will remove all rows containing NULL values from the original DataFrame.

df.fillna(130, inplace = True)

df["Calories"].fillna(130, inplace = True)

#Mode = the value that appears most frequently.

df['Date'] = pd.to_datetime(df['Date'])

df.loc[7, 'Duration'] = 45

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.duplicated())

df.drop_duplicates(inplace = True)







