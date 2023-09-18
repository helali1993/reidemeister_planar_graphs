from pyknotid.catalogue import get_knot
import networkx as nx
import pyknotid.representations as rep_
import pyknotid.make as mk
import matplotlib.pyplot as plt
from older_code.DualGraph import DualGraph
from older_code.MedialGraphBlack import MedialGraphBlack
from SignedPlanarGraph import SignedPlanarGraph

k = get_knot('4_1').space_curve()


[graph_un, duplicates, heights, first_edge]  = k.planar_diagram().as_networkx()

graph = nx.MultiGraph()

# print(graph_un.edges())

# for edge in graph_un.edges():
#     print(edge)
graph.add_edges_from(graph_un.edges())

for dup in duplicates:
    graph.add_edge(dup[0],dup[1])

# print(graph.edges())
(check, graph) = nx.check_planarity(graph)
faces_list = SignedPlanarGraph.get_faces_list(graph)
print(faces_list)

pos = nx.planar_layout(graph)

subax1 = plt.subplot(121)

nx.draw(graph, pos, node_color = 'r', with_labels=True)

plt.show()