import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\shuai.ruan\Downloads\ave_combined_output.csv")
# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 10))
df_subset = df.head(22)
# Plot 1: Br_trim
sns.lineplot(x="Max_unit", y="Gold 279 bot counts  value", data=df.head(22), ax=axes[0], label="A1", marker="v", linestyle='dotted')
sns.lineplot(x="Max_unit", y="Gold 279 bot counts  value", data=df.iloc[22:45], ax=axes[0], label="A2", marker="o", linestyle='dotted')
sns.lineplot(x="Max_unit", y="Gold 279 bot counts  value", data=df.iloc[45:68], ax=axes[0], label="A3", marker="s", linestyle='dotted')
axes[0].set_ylim(20000, 40000)
axes[0].set_xlim(0, 28)
axes[0].set_ylabel("Gold  signal per net mass g  value", fontsize=16, fontweight='bold')
axes[0].set_xlabel("")
plt.minorticks_on()
# Plot 2: bromine_207_bot_rpd_gross__value

sns.lineplot(x="Max_unit", y="Gold 279 top counts  value", data=df.head(22), ax=axes[1], label="A1", marker="v", linestyle='dotted')
sns.lineplot(x="Max_unit", y="Gold 279 top counts  value", data=df.iloc[22:45], ax=axes[1], label="A2", marker="o", linestyle='dotted')
sns.lineplot(x="Max_unit", y="Gold 279 top counts  value", data=df.iloc[45:68], ax=axes[1], label="A3", marker="s", linestyle='dotted')
axes[1].set_ylim(15000, 40000)
axes[1].set_xlim(0, 33)
axes[1].set_ylabel("Ave_Gold_279_counts_per_gram", fontsize=16, fontweight='bold')
axes[1].set_xlabel("MAX_unit", fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout()
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
# Show plot
plt.show()


