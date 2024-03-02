import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\shuai.ruan\Downloads\combined_output.csv")

# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 10))
# Plot 1: Br_trim
y1="Gold 279 bot counts  value"
filtered_A1 = df[df['Kcal_Jar'] == 'A1']
filtered_A2 = df[df['Kcal_Jar'] == 'A2']
filtered_A3 = df[df['Kcal_Jar'] == 'A3']
sns.scatterplot(x="Max_unit", y=y1, data=filtered_A1, ax=axes[0],  label="A1", marker="v", linestyle='dotted')
sns.scatterplot(x="Max_unit", y=y1, data=filtered_A2, ax=axes[0],  label="A2",marker="o", linestyle='dotted')
sns.scatterplot(x="Max_unit", y=y1, data=filtered_A3, ax=axes[0],  label="A3", marker="s", linestyle='dotted')
axes[0].set_ylim(20000, 40000)
axes[0].set_xlim(0, 28)
axes[0].set_ylabel("Gold  signal per net mass g  value", fontsize=16, fontweight='bold')
axes[0].set_xlabel("")
plt.minorticks_on()
# Plot 2: bromine_207_bot_rpd_gross__value
y2="Gold 279 top counts  value"
sns.scatterplot(x="Max_unit", y=y2, data=filtered_A1, ax=axes[1],  label="A1", marker="v", linestyle='dotted')
sns.scatterplot(x="Max_unit", y=y2, data=filtered_A2, ax=axes[1],  label="A2",marker="o", linestyle='dotted')
sns.scatterplot(x="Max_unit", y=y2, data=filtered_A3, ax=axes[1],  label="A3", marker="s", linestyle='dotted')
axes[1].set_ylim(15000, 40000)
axes[1].set_xlim(0, 28)
axes[1].set_ylabel("Ave_Gold_279_counts_per_gram", fontsize=16, fontweight='bold')
axes[1].set_xlabel("MAX_unit", fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout()
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
# Show plot
plt.show()


