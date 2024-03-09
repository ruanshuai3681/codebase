import joypy
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Sample data
data = pd.DataFrame({
    'Group': ['A'] * 100 + ['B'] * 100 + ['C'] * 100,
    'Value': np.random.randn(300)
})

# Create joyplot
fig, ax = joypy.joyplot(data, by='Group', ylim='own', figsize=(6, 4))

# Customize the plot
plt.title('Joyplot Example')
plt.xlabel('Value')
plt.ylabel('Group')
plt.show()
