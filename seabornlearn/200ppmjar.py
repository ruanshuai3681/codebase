import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\shuai.ruan\OneDrive - Chrysos Corporation Limited\Desktop\227x 100ppm gold silica jars.csv")
df.rename({"Item":"Jar_number"}, axis=1, inplace=True)
data=sns.scatterplot(x="Jar_number", y="Measured/expected ratio", data=df)#line_kws={"color": "red", "linewidth": 2.5, "alpha": 0.5})

mean_value = round(df["Measured/expected ratio"].mean(),4)
std=round(df["Measured/expected ratio"].std(), 4)
data.axhline(mean_value, color='red', linestyle='--', linewidth=2, alpha=0.9,label=f"mean_value ± std   {mean_value}±{std}")

data.axhline(mean_value + std, color='lightcoral', linestyle='--', alpha=0.1)
data.axhline(mean_value - std, color='lightcoral', linestyle='--',alpha=0.1)
plt.fill_between(list(df["Jar_number"]), mean_value+std, mean_value-std, color="lightcoral", alpha=0.3)

data.axhline(mean_value + 2*std, color='lightcoral', linestyle='--', alpha=0.1)
data.axhline(mean_value - 2*std, color='lightcoral', linestyle='--',alpha=0.1)
plt.fill_between(list(df["Jar_number"]), mean_value+2*std, mean_value-2*std, color="lightcoral", alpha=0.2)


#data.annotate(f'mean value={mean_value} \n    std={std}', xy=(200, 1), xytext=(150, 0.9), arrowprops=dict(facecolor='black', shrink=0.05,alpha=0.7), fontsize=12)

plt.ylim(0.7, 1.1)
plt.xlim(0, 230)
plt.xlabel("Jar_number", fontsize=16)
plt.ylabel("Measured/expected ratio", fontsize=16)
plt.title("200ppm gold", fontsize=16)
plt.legend(loc='lower left', fontsize=16)
plt.show()
