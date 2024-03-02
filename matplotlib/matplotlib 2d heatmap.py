import matplotlib.pyplot as plt
import numpy as np

# Generate a 2D array (matrix) for demonstration
matrix_data = np.random.rand(5, 5)

# Display the matrix using matshow
plt.matshow(matrix_data, cmap='viridis')  # Choose a colormap (e.g., 'viridis')
plt.colorbar()  # Add a colorbar for reference
plt.title('Matrix Visualization using matshow')
plt.show()
