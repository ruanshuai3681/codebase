
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Transpose the DataFrame to convert rows to columns and columns to rows
df_transposed = df.transpose()

# Reset the index to make the row labels as a new column
df_transposed.reset_index(inplace=True)

# Rename the columns
df_transposed.columns = ['new_column_name', 'values']

# Optionally, reset the index if you want to remove the original row labels
# df_transposed.reset_index(drop=True, inplace=True)

# Display the transposed DataFrame
print(df_transposed)
