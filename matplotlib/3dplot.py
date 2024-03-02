import matplotlib.pyplot as plt
import numpy as np

# Generate random 3D data
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='blue', marker='o')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.show()
