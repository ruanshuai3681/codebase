import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv(r"C:\Users\shuai.ruan\Downloads\combined_output.csv")

fig, axes = plt.subplots(3, 1, figsize=(12, 10))
filtered_242 = df[df['CRM_Jar'] == '242']
filtered_234 = df[df['CRM_Jar'] == "234"]
filtered_247 = df[df['CRM_Jar'] == "247"]

y1="Gold 279 bot counts  value per gram"
y2="Gold 279 top counts  value per gram"

sns.boxplot(x="Max_unit", y=y1, data=filtered_242, ax=axes[0])
sns.boxplot(x="Max_unit", y=y2, data=filtered_242, ax=axes[0])
#sns.scatterplot(x="Max_unit", y=y2, data=filtered_A1, ax=axes[0],  label="A1_top", marker="v", linestyle='dotted')
axes[0].set_ylim(0,8)
axes[0].set_xlim(-1, 28)
axes[0].set_ylabel("")
axes[0].legend(["KCAL_A1_bot"])

sns.boxplot(x="Max_unit", y=y1, data=filtered_247, ax=axes[1])
sns.boxplot(x="Max_unit", y=y2, data=filtered_247, ax=axes[1])
axes[1].set_ylim(0,50)
axes[1].set_xlim(-1, 28)
axes[1].set_ylabel("Gold_279_counts_per_gram", fontsize=16, fontweight='bold')
axes[1].legend(["Kcal_A2_bot"])


sns.boxplot(x="Max_unit", y=y1, data=filtered_234, ax=axes[2])
sns.boxplot(x="Max_unit", y=y2, data=filtered_234, ax=axes[2])
axes[2].set_ylim(0,1.3)
axes[2].set_xlim(-1, 28)
axes[2].set_xlabel("MAX_unit", fontsize=16, fontweight='bold')
axes[2].set_ylabel("")
axes[2].legend(["Kcal_A3_bot"])

# Adjust layout
plt.tight_layout()
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.suptitle("Gold 279 counts per gram over past 3 months Kcal", fontsize=22, y=0.97)
plt.xticks(range(0, 27, 1))
plt.show()


