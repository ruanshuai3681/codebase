# Define a function
def square(x):
    return x ** 2

# Define an iterable (list in this case)
numbers = [1, 2, 3, 4, 5]

# Apply the square function to each element of the list using map
squared_numbers = map(square, numbers)

# Convert the map object to a list (if needed) to see the results
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]

#map() is a built-in function that applies a given function to each item of an iterable (like a list, tuple, etc.) and returns an iterator that yields the results.
