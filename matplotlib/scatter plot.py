
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

plt.scatter(x_values, y_values, label='Line Plot', color="red", marker="x", alpha=1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("this is a scatter chart")
plt.legend()
plt.show()
