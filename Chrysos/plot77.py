import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv(r"C:\Users\shuai.ruan\Downloads\combined_output.csv")

fig, axes = plt.subplots(3, 1, figsize=(12, 10))
filtered_A1 = df[df['Kcal_Jar'] == 'A1']
filtered_A2 = df[df['Kcal_Jar'] == 'A2']
filtered_A3 = df[df['Kcal_Jar'] == 'A3']

y1="Gold 279 bot counts  value per gram"
y2="Gold 279 top counts  value per gram"

sns.barplot(x="Max_unit", y=y1, data=filtered_A1, ax=axes[0],  label="KCAL_A1_bot")
sns.barplot(x="Max_unit", y=y2, data=filtered_A1, ax=axes[0],  label="KCAL_A1_top")
axes[0].set_ylim(0,80)
axes[0].set_xlim(-1, 28)
axes[0].set_ylabel("")
axes[0].set_xlabel("")


sns.barplot(x="Max_unit", y=y1, data=filtered_A2, ax=axes[1],  label="KCAL_A2_bot")
sns.barplot(x="Max_unit", y=y2, data=filtered_A2, ax=axes[1],  label="KCAL_A2_top")
axes[1].set_ylim(0,80)
axes[1].set_xlim(-1, 28)
axes[1].set_ylabel("Gold_279_counts_per_gram", fontsize=16, fontweight='bold')
axes[1].set_xlabel("")


sns.barplot(x="Max_unit", y=y1, data=filtered_A3, ax=axes[2],  label="KCAL_A3_bot")
sns.barplot(x="Max_unit", y=y2, data=filtered_A3, ax=axes[2],  label="KCAL_A3_top")
axes[2].set_ylim(0,80)
axes[2].set_xlim(-1, 28)
axes[2].set_xlabel("MAX_unit", fontsize=16, fontweight='bold')
axes[2].set_ylabel("")


# Adjust layout
plt.tight_layout()
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.suptitle("Gold 279 counts per gram over past 3 months Kcal", fontsize=22, y=0.97)
plt.xticks(range(0, 28, 1))
plt.show()


