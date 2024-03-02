from bokeh.plotting import figure, show
import numpy as np

# Create some sample data
x = np.random.randn(100)
y = np.random.randn(100)
# Create a scatter plot
p = figure(title="Scatter Plot Example", x_axis_label="X-axis", y_axis_label="Y-axis")
p.circle(x, y, size=10, color="navy", alpha=0.5)

show(p)
