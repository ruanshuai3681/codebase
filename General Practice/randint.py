import numpy as np

# Generate a random integer between 0 and 9
random_number = np.random.randint(10)
print(random_number)

# Generate an array of 5 random integers between 1 and 10
random_array = np.random.randint(1, 11, size=5)
print(random_array)

# Generate a 3x3 array of random integers between -5 and 5
random_matrix = np.random.randint(-5, 6, size=(3, 3))
print(random_matrix)

np.random.choice(random_array, size=(3,3), replace=True, p=None)
# replace: Whether the sampling is done with or without replacement.
# If True, the same element can be chosen more than once.
# If False, each element can only be chosen once.
