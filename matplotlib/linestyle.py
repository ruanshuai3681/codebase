import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = "dotted", c="r", lw=2)
plt.show()

#linestyle can be written as ls.

#dotted can be written as :.

#dashed can be written as --.

#You can use the keyword argument color or the shorter c to set the color of the line:

#You can use the keyword argument linewidth or the shorter lw to change the width of the line.
