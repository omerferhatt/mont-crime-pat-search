# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time


def create_grid(values, b_box, threshold=0.4, grid_size=0.002, plot=False):
    """
    Creates grid view to look at the points regionally.

    :param values: Crime points, 2D array
    :param b_box: Coordinates of the geogr. location, 2D Array
    :param threshold: Threshold value between 0 and 1, Float
    :param grid_size: Step size to grid points, Float
    :param plot: Boolean value to plotting grid view and heat map graphs. Boolean

    :return: Grid, if Plot enabled returns plot elements too (fig, axes etc.)
    """
    print("\t\tCreating Grid:")
    grid_size = grid_size
    x_grid = np.arange(b_box[0], b_box[2], grid_size)
    y_grid = np.arange(b_box[1], b_box[3], grid_size)
    # Creating empty grid
    grid = np.zeros((len(x_grid) - 1, len(y_grid) - 1))
    print(f"Grid step: {grid_size} x {grid_size}")
    print(f"Grid shape: {grid.shape[0]}x{grid.shape[1]}")
    print(f"Grid threshold: {threshold}")
    # Creating mesh to search all points in all grid axis
    xx = np.array([x_grid[:-1], x_grid[1:]]).T
    yy = np.array([y_grid[:-1], y_grid[1:]]).T
    # Starting time from now
    a = time.time()
    # All elements in values are starting to be seen
    for point_x, point_y in values:
        for i, x_pt in enumerate(xx):
            for k, y_pt in enumerate(yy):
                if (y_pt[0] < point_x <= y_pt[1]) and (x_pt[0] < point_y <= x_pt[1]):
                    # If crime happens, it votes to grid
                    grid[i, k] += 1
                    break
            else:
                continue
            break
        else:
            continue

    # Timing stopped and printing results
    b = time.time()
    print(f"Grid created in: {b - a} sec")
    # Calculating standard deviation and average of axis
    print(f"Average of grid: {np.mean(grid)}")
    print(f"Standart deviation on all grid: {np.std(grid, axis=None)}")
    std_x = np.std(grid, axis=0)
    std_y = np.std(grid, axis=1)
    for i, std in enumerate(zip(std_x, std_y)):
        print(f"Standart deviation on {i}|\t x axis: {std[0]:.3f} |\t y axis: {std[1]:3f}")

    # Min-Max scaling on grid to work
    grid_temp = grid
    grid_max = np.max(grid)
    # Threshold array
    grid = grid / grid_max
    grid[grid < threshold] = 0
    grid[grid >= threshold] = 1
    # Plotting binary grid and heatmap
    if plot:
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        axes[0].set_xticks(np.arange(0, grid.shape[0]))
        axes[0].set_yticks(np.arange(0, grid.shape[1]))
        axes[0].imshow(grid, interpolation="nearest")

        sns.heatmap(grid_temp, linewidth=0.5, ax=axes[1])
        plt.show(block=False)
        return grid, fig, axes

    return grid

