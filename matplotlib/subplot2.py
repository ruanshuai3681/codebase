import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot
axs[0, 0].plot(x, y1, label='sin(x)', color='blue')
axs[0, 0].set_title('Sine Function')
axs[0, 0].legend()

axs[0, 1].plot(x, y2, label='cos(x)', color='orange')
axs[0, 1].set_title('Cosine Function')
axs[0, 1].legend()

axs[1, 0].plot(x, y3, label='tan(x)', color='green')
axs[1, 0].set_title('Tangent Function')
axs[1, 0].legend()

# Add an empty subplot in the last position
axs[1, 1].axis('off')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
