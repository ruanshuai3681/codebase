import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\shuai.ruan\PycharmProjects\shuai_ruan\20240223_trim_data.csv")
df.rename({"analysis_parameters__reference_trim__1": "Br_trim"}, axis=1, inplace=True)
df["MAX_unit"] = df['unit'].str[3:].astype(int)
df["rpdxxtrim"] = df["Br_trim"] * df["bromine_207_bot_rpd_gross__value"]

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Br_trim
sns.scatterplot(x="MAX_unit", y="Br_trim", data=df, ax=axes[0, 0])
axes[0, 0].set_ylim(0.5, 1.5)
axes[0, 0].set_xlim(0, 27)
axes[0, 0].set_ylabel("AXD_Br_Trim", fontsize=16)

# Plot 2: rpdxxtrim
sns.scatterplot(x="MAX_unit", y="rpdxxtrim", data=df, ax=axes[0, 1])
axes[0, 1].set_ylim(4000, 10000)
axes[0, 1].set_xlim(0, 27)
axes[0, 1].set_ylabel("AXD_Br_Trim", fontsize=16)

# Plot 3: bromine_207_bot_rpd_gross__value
sns.scatterplot(x="MAX_unit", y="bromine_207_bot_rpd_gross__value", data=df, ax=axes[1, 0])
axes[1, 0].set_ylim(4000, 10000)
axes[1, 0].set_xlim(0, 27)
axes[1, 0].set_ylabel("Br_207_bot_rpd_gross", fontsize=16)

# Set minor ticks
for ax in axes.flat:
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(500))

# Add labels
axes[1, 0].set_xlabel("MAX_Unit", fontsize=16)
axes[1, 1].set_xlabel("MAX_Unit", fontsize=16)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
