import numpy as np
import matplotlib.pyplot as plt

data=np.random.uniform(0.0, 5.0, 1000)
plt.hist(data, 50)
plt.show()
