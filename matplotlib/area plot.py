import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y1_values = [2]
y2_values = [3]

plt.fill_between(x_values, y1_values, y2_values, color="red", alpha=0.6, label="fill area")
plt.xlabel("this is x")
plt.ylabel("this is y")
plt.legend()
plt.title("fill")
plt.show()
