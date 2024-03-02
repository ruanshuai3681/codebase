from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import numpy as np

# Generate sample data
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

# Create a Bokeh figure
p = figure(title="Area Chart Example", x_axis_label="X-axis", y_axis_label="Y-axis", width=800, height=400)

# Add area plot
p.patch(x=np.concatenate([x, x[::-1]]), y=np.concatenate([y, np.zeros_like(y[::-1])]), color="green", alpha=0.4, line_color="black")

# Display the plot in a Jupyter notebook (optional)

show(p)

