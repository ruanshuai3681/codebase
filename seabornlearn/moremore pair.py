import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
titanic = sns.load_dataset("titanic")

# Create pairplot with hue and additional customization
sns.pairplot(titanic, hue="survived", palette="husl", markers=["o", "s"], diag_kind="kde", diag_kws={"shade": True, "bw_adjust": 0.8})

# Show plot
plt.show()
