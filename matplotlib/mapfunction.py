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
