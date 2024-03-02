import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\shuai.ruan\Downloads\20240223_trim_data - Copy.csv")
df.rename({"analysis_parameters__reference_trim__6": "Tb_trim"}, axis=1, inplace=True)
df["MAX_unit"] = df['unit'].str[3:].astype(int)

# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Br_trim
sns.scatterplot(x="MAX_unit", y="Tb_trim", data=df, ax=axes[0])
axes[0].set_ylim(0, 6)
axes[0].set_xlim(0, 27)
axes[0].set_ylabel("AXD_Tb_Trim", fontsize=16)
axes[0].set_xlabel("")
# Plot 2: bromine_207_bot_rpd_gross__value
sns.scatterplot(x="MAX_unit", y="terbium_45_bot_rpd_gross__value", data=df, ax=axes[1])
axes[1].set_ylim(0, 850)
axes[1].set_xlim(0, 27)
axes[1].set_ylabel("Tb_45_bot_rpd_gross", fontsize=16)
axes[1].set_xlabel("MAX_Unit", fontsize=16)

# Adjust layout
plt.tight_layout()
plt.suptitle("AXC_Tb_Trim, 0.133g TbO per disc", fontsize=24, y=0.97)
# Show plot
plt.show()


