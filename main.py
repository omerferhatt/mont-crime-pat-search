# Library imports
import sys
import numpy as np

# User defined library imports
from file_read import read_shp, get_values
from grid import create_grid
from a_star import search
from prompt_read import read_search_prompt, read_grid_prompt


# Locate file pats
path = "shape/crime_dt"
# Get data's into data frame
df, bbox = read_shp(path)
# Convert it into numpy array to work with
values = get_values(df, np.float32)
# Get grid configuration from user input
grid_size, threshold = read_grid_prompt()
# Create grid with crime points
grid, fig, ax = create_grid(values, bbox, threshold=threshold, grid_size=grid_size, plot=True)
# Get search start end points from user input
start, end = read_search_prompt(grid)
# Define costs
cost = [1, 1.3, 1.5]
# Search for optimal path
path = search(grid, cost, start, end, [fig, ax])
