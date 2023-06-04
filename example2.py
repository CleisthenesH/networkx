import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial import Voronoi
import numpy as np

# Generate a point cloud
rng = np.random.default_rng(seed = 1)
points_cloud = rng.random((10,2))

# Calculate the Voronoi Cells
vor = Voronoi(points_cloud)
    
# Brach for the scipy's inbuild rendering of Voronoi Cells (But not nerves).
if 1:
    # G is the main graph which shows the nerve
    G = nx.Graph()

    # Transpose postion data for nice rendering
    pos = {}
    for idx, point in enumerate(points_cloud):
        pos[idx] = point

    # Extract node and edge data for the nerve
    G.add_nodes_from((range(len(points_cloud))))
    G.add_edges_from(vor.ridge_points)

    # V is a secondary graph of internal Voronoi Cells
    V = nx.Graph()

    # Transpose postion data for nice rendering
    v_pos = {}
    for idx, point in enumerate(vor.vertices):
        v_pos[idx] = point

    # Extracts nodes and edge data for Voronoi Cells (filter out edges)
    V.add_nodes_from(range(len(vor.vertices)))
    V.add_edges_from(x for x in vor.ridge_vertices if x[0] != -1 and x[1] != -1)

    # Draw the main graph
    nx.draw_networkx_nodes(G, pos, node_size=10)
    nx.draw_networkx_edges(G, pos, edge_color = "gray", width = 1)

    # Draw the secondary graph
    nx.draw_networkx_nodes(V, v_pos, node_color = "red", node_size=10)
    nx.draw_networkx_edges(V, v_pos, edge_color = "red", width = 1)
    
    # show plt
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
else:
    # Load and use the scipy's inbuild voronoi_plot_2d
    from scipy.spatial import voronoi_plot_2d
    fig = voronoi_plot_2d(vor)

    # show plt
    plt.show()
