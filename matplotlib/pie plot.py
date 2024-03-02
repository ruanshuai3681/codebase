
import matplotlib.pyplot as plt

labels = ['Label A', 'Label B', 'Label C']
sizes = [30, 45, 25]
explode=(0.2, 0, 0)
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, shadow=True, explode=explode, colors=["blue", "red","yellow"])
plt.title("pie chart")

plt.show()
