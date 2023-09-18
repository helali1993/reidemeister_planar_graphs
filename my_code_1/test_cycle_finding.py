import networkx as nx
from SignedPlanarGraph import SignedPlanarGraph

def multigraph_to_graph(multi_graph):
    graph = nx.Graph()
    for u, v, key, data in multi_graph.edges(data=True, keys=True):
        graph.add_edge(u, v)
    return graph

# Create a multigraph (replace this with your own multigraph)
# multi_graph = nx.MultiGraph()
# multi_graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (3, 5), (5, 6), (6, 3), (1, 2)])

# Convert the multigraph to a graph
# graph = multigraph_to_graph(multi_graph)

# # Now you can use cycle_basis on the graph
# cycles = nx.cycle_basis(graph)
# print("Cycles:", cycles)

face = [1,2,0,4,5]
next_face = [0,0]

[cond, edge] = SignedPlanarGraph.check_same_edge_region(face, next_face)

print(cond)
print(edge)
