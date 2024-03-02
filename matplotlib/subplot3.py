import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = x ** 2
data = np.random.normal(0, 1, 100)

# Create subplots with different types
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Subplot 1: Line plot
axs[0, 0].plot(x, y1, label='sin(x)', color='blue')
axs[0, 0].set_title('Line Plot')
axs[0, 0].legend()

# Subplot 2: Scatter plot
axs[0, 1].scatter(x, y2, label='x^2', color='red', marker='o')
axs[0, 1].set_title('Scatter Plot')
axs[0, 1].legend()

# Subplot 3: Bar plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 1, 5]
axs[1, 0].bar(categories, values, color='green')
axs[1, 0].set_title('Bar Plot')

# Subplot 4: Histogram
axs[1, 1].hist(data, bins=20, color='purple', edgecolor='black')
axs[1, 1].set_title('Histogram')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
