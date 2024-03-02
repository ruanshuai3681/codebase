import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Create a box plot of 'total_bill' for each 'day'
sns.boxplot(data=tips, x="day", y="total_bill")

# Show the plot
plt.show()
