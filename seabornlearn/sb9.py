import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')

# Create a scatter plot with a linear fit
ax = sns.regplot(x='total_bill', y='tip', data=tips)

# Get the coefficients of the linear regression
slope, intercept = ax.get_lines()[0].get_data()

# Format slope and intercept to three decimal points
slope_formatted = format(slope, '.3f')
intercept_formatted = format(intercept, '.3f')

# Create the equation string
equation = f'y = {slope_formatted}x + {intercept_formatted}'

# Add annotation for the equation
ax.text(25, 6, equation, fontsize=12, color='red')

# Set the labels and title
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Scatter Plot with Linear Fit and Fitting Function')

# Show the plot
plt.show()
