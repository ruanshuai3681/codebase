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

sns.barplot(x="Max_unit", y=y1, data=filtered_242, ax=axes[0],  label="Oreas_242_bot")
sns.barplot(x="Max_unit", y=y2, data=filtered_242, ax=axes[0],  label="Oreas_242_bot")
axes[0].set_ylim(0,8)
axes[0].set_xlim(-1, 28)
axes[0].set_ylabel("")
axes[0].set_xlabel("")


sns.barplot(x="Max_unit", y=y1, data=filtered_247, ax=axes[1],  label="Oreas_247_bot")
sns.barplot(x="Max_unit", y=y2, data=filtered_247, ax=axes[1],  label="Oreas_247_bot")
axes[1].set_ylim(0,50)
axes[1].set_xlim(-1, 28)
axes[1].set_ylabel("Gold_279_counts_per_gram", fontsize=16, fontweight='bold')
axes[1].set_xlabel("")


sns.barplot(x="Max_unit", y=y1, data=filtered_234, ax=axes[2],  label="Oreas_234_bot")
sns.barplot(x="Max_unit", y=y2, data=filtered_234, ax=axes[2],  label="Oreas_234_top")
axes[2].set_ylim(0,1.3)
axes[2].set_xlim(-1, 28)
axes[2].set_xlabel("MAX_unit", fontsize=16, fontweight='bold')
axes[2].set_ylabel("")


# Adjust layout
plt.tight_layout()
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.suptitle("Gold 279 counts per gram over past 3 months", fontsize=22, y=0.97)
plt.xticks(range(0, 28, 1))
plt.show()


