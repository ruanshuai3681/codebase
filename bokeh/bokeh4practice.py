from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool
import numpy as np

# Generate some sample data
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Create a Bokeh figure
p = figure(title="Interactive Line Plot", x_axis_label="X-axis", y_axis_label="Y-axis", width=800, height=500)

# Plot the line
line = p.line(x, y, line_width=2, line_color="blue")

# Add interactive tooltips
hover = HoverTool(renderers=[line], tooltips=[("X", "@x"), ("Y", "@y")], mode='vline')
p.add_tools(hover)

show(p)

