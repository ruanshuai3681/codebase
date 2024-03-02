import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
titanic = sns.load_dataset("titanic")

# Create a bar plot of survival counts by 'class'
sns.barplot(data=titanic, x="class", y="survived", ci=None)

# Show the plot
plt.show()
