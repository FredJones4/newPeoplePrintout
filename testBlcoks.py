import numpy as np

# Example arrays of points
x = np.array([1, 2, 3, 4])
y = np.array([4, 3, 2, 1])

# The point for which we want to calculate the distance
x_idx = 0
y_idx = 0

# Compute the Euclidean distance from (x_idx, y_idx) to each point in arrays x and y
distances = np.sqrt((x - x_idx)**2 + (y - y_idx)**2)

# Print the distances
print(distances)
