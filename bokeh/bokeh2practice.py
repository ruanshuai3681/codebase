import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category10_10

# Generate random data
x = np.linspace(-10, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

# Create a ColumnDataSource
source = ColumnDataSource(data={'x': x, 'y1': y1, 'y2': y2, 'y3': y3})

# Create a Bokeh figure
p = figure(title="Multiple Lines Example", x_axis_label="X-axis", y_axis_label="Y-axis")

# Plot multiple lines
p.line('x', 'y1', source=source, line_width=2, line_color=Category10_10[0], legend_label='sin(x)')
p.line('x', 'y2', source=source, line_width=2, line_color=Category10_10[1], legend_label='cos(x)')
p.line('x', 'y3', source=source, line_width=2, line_color=Category10_10[2], legend_label='sin(x) + cos(x)')

# Add legend
p.legend.location = "top_left"
p.legend.click_policy = "hide"  # Clicking on legend items will hide/show the corresponding line

show(p)


