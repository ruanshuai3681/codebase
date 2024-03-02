import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Create a histogram with KDE plot of the 'total_bill' column
#sns.histplot(data=tips, x="total_bill", kde=True)
sns.scatterplot(x='total_bill', y='tip', data=tips, palette='viridis')
#print(tips.head())
# Show the plot
plt.show()
