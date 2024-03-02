import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Create a violin plot of 'total_bill' vs 'day'
sns.violinplot(data=tips, x="day", y="total_bill")

# Show the plot
plt.show()
