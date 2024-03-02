import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r', ms=10, mec="k", mfc="c")# k for black, c for cyan
plt.show()

#This parameter is also called fmt, and is written with this syntax:
#marker|line|color
#-, :, --, -.
#markersize or the shorter version, ms to set the size of the markers:
#You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
#You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
