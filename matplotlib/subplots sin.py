import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(x, y1, label='sin(x)')
ax2.plot(x, y2, label='cos(x)', color='orange')

ax1.legend()
ax2.legend()
plt.show()
#fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True):
# Creates a figure (fig) and two subplots (ax1 and ax2) arranged in two rows and one column.
# The sharex=True parameter ensures that both subplots share the same x-axis.
