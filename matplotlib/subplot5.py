import matplotlib.pyplot as plt

# Create a new figure
fig = plt.figure()

# Add multiple subplots in a grid
ax1 = fig.add_subplot(221)  # 2 rows, 2 columns, subplot 1
ax2 = fig.add_subplot(222)  # 2 rows, 2 columns, subplot 2
ax3 = fig.add_subplot(223)  # 2 rows, 2 columns, subplot 3
ax4 = fig.add_subplot(224)  # 2 rows, 2 columns, subplot 4

# Customize each subplot
ax1.plot([1, 2, 3])
ax2.scatter([1, 2, 3], [4, 5, 6])
ax3.bar(['A', 'B', 'C'], [7, 8, 9])
ax4.hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Show the plot
plt.show()
