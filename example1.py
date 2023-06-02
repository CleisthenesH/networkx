import matplotlib.pyplot as plt
import networkx as nx

# load demo data
G = nx.karate_club_graph()

# generator for the complete graph for each clique of size 4
cliques = ( [(u,v) for u in clique for v in clique] for clique in nx.find_cliques(G) if len(clique) == 4)

# position the graph in a human readable way
pos = nx.spring_layout(G)

# draw nodes
nx.draw_networkx_nodes(G, pos, node_size=10)

# draw edges
nx.draw_networkx_edges(G, pos, edge_color = "gray", width = 1)

# draw the cliques of size 4
for clique in cliques:
    nx.draw_networkx_edges(G,pos,edgelist=clique,edge_color = "r", width = 2)

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size = 5)

# show plt
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
