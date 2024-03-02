import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load and display an image using Seaborn
img = mpimg.imread('../matplotlib/example_image.png')
sns.heatmap(img[:, :, 0])  # Display the first channel of the image as a heatmap
plt.axis('on')  # Turn off axis labels and ticks
plt.show()
