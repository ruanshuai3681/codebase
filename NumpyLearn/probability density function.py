from numpy import random
import matplotlib.pyplot as plt

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

plt.hist(x, label="ppp", color="red")
plt.xlabel("elements")
plt.ylabel("probability")
plt.legend()
plt.show()


