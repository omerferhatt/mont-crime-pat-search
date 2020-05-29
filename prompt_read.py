# Library imports
import sys
import re

# Get grid configuration from user prompt
def read_grid_prompt():
    grid_size = float(input("Please enter grid step (0.002 default):"))
    grid_thresh = float(input("Please enter grid threshold value (0.4 default):"))

    return grid_size, grid_thresh


# Get search algorithm parameters from user prompt
def read_search_prompt(grid):
    print("Please enter starting point e.g. >>> 3,12\n")
    start = input()
    start = tuple(int(i) for i in re.sub(r"\s+", "", start).split(","))
    while grid[start[::-1]] == 1:
        print("Entered filled block please enter start point again e.g. >>> 10,3\n")
        start = input()
        start = tuple(int(i) for i in re.sub(r"\s+", "", start).split(","))

    print("Please enter end point e.g. >>> 7,4\n")
    end = input()
    end = tuple(int(i) for i in re.sub(r"\s+", "", end).split(","))
    while grid[end[::-1]] == 1:
        print("Entered filled block please enter end point again e.g. >>> 2,5\n")
        end = input()
        end = tuple(int(i) for i in re.sub(r"\s+", "", end).split(","))

    return start, end
