from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool
import numpy as np
from bokeh.palettes import Category10_10
import pandas as pd
data=pd.read_json(r"C:\Users\shuai.ruan\OneDrive - Chrysos Corporation Limited\Desktop\spectra.json")

p = figure(title="Interactive Scatter Plot", x_axis_label="X-axis", y_axis_label="Y-axis", width=800, height=400)
