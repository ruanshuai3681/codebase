import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
iris = sns.load_dataset("iris")

# Create a pair plot of the numeric columns
sns.pairplot(iris,hue='species')

# Show the plot
plt.show()
