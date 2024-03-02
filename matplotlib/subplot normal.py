import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random samples from a normal distribution with mean 0 and standard deviation 1
random_samples = np.random.normal(loc=0, scale=1, size=1000)

# Plot histograms with and without density normalization
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(random_samples, bins=30, color='blue', alpha=0.7)
plt.title('Histogram without Density Normalization')

plt.subplot(1, 2, 2)
plt.hist(random_samples, bins=30, density=True, color='green', alpha=0.7)
plt.title('Histogram with Density Normalization')

plt.tight_layout()
plt.show()
