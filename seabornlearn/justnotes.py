# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
sns.scatterplot(x='total_bill', y='tip', data=tips, ax=axes[0, 1])
axes[0, 1].set_title('Tip vs Total Bill')
