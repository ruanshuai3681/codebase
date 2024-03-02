import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create FacetGrid object
g = sns.FacetGrid(tips, col="time", row="sex", margin_titles=True)

# Map plots to the grid
g.map(sns.scatterplot, "total_bill", "tip")

# Add titles
g.fig.suptitle('Tip vs Total Bill by Time and Sex', size=16)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust subplot layout to fit suptitle

# Show plots
plt.show()
