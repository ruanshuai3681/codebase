from bokeh.plotting import figure, show

# Create a Bokeh figure
p = figure(title="Example Plot", x_axis_label="X-axis", y_axis_label="Y-axis")

# Add a line renderer
line_renderer = p.line(x=[1, 2, 3, 4, 5], y=[6, 7, 2, 4, 5], line_width=2, line_color="blue")

# Add a circle renderer
circle_renderer = p.circle(x=[1, 2, 3, 4, 5], y=[6, 7, 2, 4, 5], size=10, fill_color="red", line_color="black")

# Display the plot
show(p)
