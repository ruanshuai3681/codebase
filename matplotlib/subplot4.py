import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x + np.random.normal(0, 1, len(x))

# Create a grid of subplots with custom layout
fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(3, 3, width_ratios=[1, 2, 1], height_ratios=[1, 2, 1])

# Subplot 1: Line plot
ax1 = plt.subplot(gs[0, 1])
ax1.plot(x, y1, label='sin(x)', color='blue')
ax1.set_title('Line Plot')
ax1.legend()

# Subplot 2: Scatter plot
ax2 = plt.subplot(gs[1, 0])
ax2.scatter(x, y3, label='x + noise', color='red', marker='o')
ax2.set_title('Scatter Plot')
ax2.legend()

# Subplot 3: Heatmap
ax3 = plt.subplot(gs[1, 1])
heatmap_data = np.random.rand(10, 10)
cax = ax3.imshow(heatmap_data, cmap='viridis', interpolation='none', aspect='auto')
ax3.set_title('Heatmap')
fig.colorbar(cax, ax=ax3)

# Subplot 4: Cosine function
ax4 = plt.subplot(gs[1, 2])
ax4.plot(x, y2, label='cos(x)', color='green')
ax4.set_title('Cosine Function')
ax4.legend()

# Subplot 5: Histogram
ax5 = plt.subplot(gs[2, 1])
ax5.hist(y3, bins=20, color='purple', edgecolor='black')
ax5.set_title('Histogram')

# Remove unused subplots
fig.delaxes(plt.subplot(gs[0, 0]))
fig.delaxes(plt.subplot(gs[0, 2]))
fig.delaxes(plt.subplot(gs[2, 0]))
fig.delaxes(plt.subplot(gs[2, 2]))

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
