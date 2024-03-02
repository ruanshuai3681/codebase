import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\shuai.ruan\Downloads\20240223_trim_data - Copy.csv")
df.rename({"analysis_parameters__reference_trim__1": "Br_trim"}, axis=1, inplace=True)
df["MAX_unit"] = df['unit'].str[3:].astype(int)

# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Br_trim
sns.scatterplot(x="MAX_unit", y="Br_trim", data=df, ax=axes[0])
axes[0].set_ylim(0.7, 1.4)
axes[0].set_xlim(0, 27)
axes[0].set_ylabel("AXC_Br_Trim", fontsize=16, fontweight='bold')
axes[0].set_xlabel("")
plt.minorticks_on()
# Plot 2: bromine_207_bot_rpd_gross__value
sns.scatterplot(x="MAX_unit", y="bromine_207_bot_rpd_gross__value", data=df, ax=axes[1])
axes[1].set_ylim(4000, 9500)
axes[1].set_xlim(0, 27)
axes[1].set_ylabel("Br_207_bot_rpd_gross", fontsize=16, fontweight='bold')
axes[1].set_xlabel("MAX_Unit", fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout()
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.suptitle("AXC_Br_Trim, 0.32g RbBr per disc", fontsize=24, y=0.97)
# Show plot
plt.show()


