import matplotlib.pyplot as plt

x=["a", "b","c","d"]
y=[1,2,3,4]


plt.plot(x, y, label="this is a label", color="skyblue", marker="s")
plt.xlabel("xx")
plt.ylabel("yy")

plt.title("this is a title")
plt.legend()
plt.show()
