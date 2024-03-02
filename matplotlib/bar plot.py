import matplotlib.pyplot as plt

cat=["a","b","c","d"]
value=[1,2,3,4]

plt.bar(cat,value, label="this is a label", color="pink", alpha=1)
plt.title("bar chart")
plt.xlabel('cat')
plt.ylabel("value")
plt.legend()
plt.show()

