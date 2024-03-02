import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\shuai.ruan\PycharmProjects\shuai_ruan\20240223_trim_data.csv")
df["MAX_unit"] = df['unit'].str[3:].astype(int)

# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1:
sns.scatterplot(x="MAX_unit", y="linac_energy_mev__value", data=df, ax=axes[0])
axes[0].set_ylim(8.2, 8.8)
axes[0].set_xlim(0, 27)
axes[0].set_ylabel("linac_energy", fontsize=16)
axes[0].set_xlabel("")
# Plot 2: bromine_207_bot_rpd_gross__value
sns.scatterplot(x="MAX_unit", y="linac_output__value", data=df, ax=axes[1])
axes[1].set_ylim(4500, 8500)
axes[1].set_xlim(0, 27)
axes[1].set_ylabel("linac_output", fontsize=16)
axes[1].set_xlabel("MAX_Unit", fontsize=16)

# Adjust layout
plt.tight_layout()
plt.suptitle("Linac over two weeks", fontsize=24, y=0.97)
# Show plot
plt.show()
