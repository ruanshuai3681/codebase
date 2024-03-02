import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load and display an image using Matplotlib
img = mpimg.imread('example_image.png')
plt.imshow(img)
plt.axis('on')  # Turn off axis labels and ticks
plt.show()


