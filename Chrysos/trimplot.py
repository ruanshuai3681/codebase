import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\shuai.ruan\PycharmProjects\shuai_ruan\20240223_trim_data.csv")
df.rename({"analysis_parameters__reference_trim__1":"Br_trim"}, axis=1, inplace=True)
df["MAX_unit"]=df['unit'].str[3:].astype(int)
df["rpdxxtrim"]=df["Br_trim"]*df["bromine_207_bot_rpd_gross__value"]

fig, axes = plt.subplots(2, 1, figsize=(12, 10))

Br_trim=sns.scatterplot(x="MAX_unit", y="Br_trim", data=df, ax=axes[0,0])#line_kws={"color": "red", "linewidth": 2.5, "alpha": 0.5})
plt.ylim(0.5, 1.5)
plt.xlim(0, 27)
plt.ylabel("AXD_Br_Trim", fontsize=16)

RPDxtrim=sns.scatterplot(x="MAX_unit", y="rpdxxtrim", data=df, ax=axes[0,1])#line_kws={"color": "red", "linewidth": 2.5, "alpha": 0.5})
plt.ylim(4000, 10000)
plt.xlim(0, 27)
plt.ylabel("AXD_Br_Trim", fontsize=16)


Br_207_bot_rpd_gross=sns.scatterplot(x="MAX_unit", y="bromine_207_bot_rpd_gross__value", data=df, ax=axes[1,0])
plt.ylim(4000, 10000)
plt.xlim(0, 27)
plt.ylabel("Br_207_bot_rpd_gross", fontsize=16)

plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.minorticks_on()
plt.xlabel("MAX_Unit", fontsize=16)
plt.show()
