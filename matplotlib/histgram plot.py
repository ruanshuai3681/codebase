import matplotlib.pyplot as plt
import numpy

data= numpy.random.randn(1000)

plt.hist(data, bins=100, color="skyblue", alpha=0.9, label="this is the legend")
plt.xlabel("xx")
plt.ylabel("yy")

plt.title("this is a title")
plt.legend()
plt.show()
