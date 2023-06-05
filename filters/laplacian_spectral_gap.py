import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial import Voronoi
import numpy as np

# Generate a point cloud
rng = np.random.default_rng(seed = 1)
points_cloud = rng.random((10,2))

# Calculate the Voronoi Cells
vor = Voronoi(points_cloud)

# G is the main graph which shows the nerve
G = nx.Graph()

# Extract node and edge data for the nerve
G.add_nodes_from(range(len(points_cloud)))
G.add_edges_from(vor.ridge_points)

# Calculate the Laplacian Spectrum
laplacian = nx.laplacian_spectrum(G)

# Initalize values for the largest, second largest, and smallest moduli of eigenvalues
modulus = np.abs(laplacian[0])

max_1 = modulus
max_2 = modulus
min_1 = modulus

# Extract the desired moduli from the spectrum 
for eigen in laplacian:
    modulus = np.abs(eigen)

    if modulus > max_2:
        if modulus > max_1:
            max_2 = max_1
            max_1 = eigen
        else:
            max_2 = eigen
    
    if modulus < min_1:
        min_1 = modulus

# Print out the Moduli
print("Smallest Modulus:", min_1)
print("Largest Modulus:", max_1)
print("Second Largest Modulus:", max_2)
print("Difference:", max_1-max_2)

# Example output:
#
# Smallest Modulus: 7.24950623116108e-16
# Largest Modulus: 7.479326945646297
# Second Largest Modulus: 6.308900754238791
# Difference: 1.1704261914075058
