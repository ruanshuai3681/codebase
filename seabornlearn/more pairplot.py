import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset("iris")

# Create pairplot with hue
sns.pairplot(iris, hue="species")

# Show plot
plt.show()
