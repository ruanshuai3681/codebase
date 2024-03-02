from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool
import numpy as np
from bokeh.palettes import Category10_10
# Generate some sample data
np.random.seed(42)
x = np.random.rand(100)
y = np.random.rand(100)
size = np.random.randint(5, 35, 100)
color = np.random.choice(Category10_10, 100)

# Create a Bokeh figure
p = figure(title="Interactive Scatter Plot", x_axis_label="X-axis", y_axis_label="Y-axis", width=800, height=400)

# Plot the scatter points
scatter = p.scatter(x, y, size=size, color=color, alpha=0.6) 

# Add interactive tooltips
hover = HoverTool(renderers=[scatter], tooltips=[("X", "@x"), ("Y", "@y"), ("Size", "@size"), ("Color", "@color")])
p.add_tools(hover)


show(p)
