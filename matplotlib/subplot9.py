import matplotlib.pyplot as plt

fig=plt.figure()

ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)

ax1.plot([1, 2, 3])
ax2.scatter([1, 2, 3], [4, 5, 6])
ax3.bar(['A', 'B', 'C'], [7, 8, 9])
ax4.hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

plt.show()
