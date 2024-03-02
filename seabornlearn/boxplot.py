import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a figure with three subplots arranged vertically
fig, axes = plt.subplots(3, 1, figsize=(8, 12))

# Plot 1 (Top subplot)
sns.histplot(tips['total_bill'], kde=True, ax=axes[0])
axes[0].set_title('Histogram of Total Bill')

# Plot 2 (Middle subplot)
sns.scatterplot(x='total_bill', y='tip', data=tips, ax=axes[1])
axes[1].set_title('Tip vs Total Bill')

# Plot 3 (Bottom subplot)
sns.boxplot(x='day', y='total_bill', data=tips, ax=axes[2])
axes[2].set_title('Total Bill by Day')

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()
