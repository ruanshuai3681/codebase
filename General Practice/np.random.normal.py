import numpy as np

# Generate 1000 random samples from a normal distribution with mean 0 and standard deviation 1
random_samples = np.random.normal(loc=0, scale=1, size=1000)

# Plot a histogram of the generated samples
import matplotlib.pyplot as plt
plt.hist(random_samples, bins=30, density=True, alpha=0.7, color='blue')
plt.title('Random Samples from a Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
#the density=True parameter normalizes the histogram,
# making the total area under the histogram equal to 1.
# When density is set to True, the y-axis represents the probability density rather than the raw count
