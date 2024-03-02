import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\shuai.ruan\OneDrive - Chrysos Corporation Limited\Desktop\227x 100ppm gold silica jars.csv")
filtered_df=df[df["gross_mass"]>320]
sns.lmplot(x="gross_mass", y="PA gold grade", data=filtered_df)
plt.show()
