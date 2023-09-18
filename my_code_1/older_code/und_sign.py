from pyknotid.catalogue import get_knot
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph

k = get_knot('4_1').space_curve()


[graph_un, duplicates, heights, first_edge]  = k.planar_diagram().as_networkx()

print("------------------------------")
print("Nodes:")
print(graph_un.nodes())
print("------------------------------")
print("Edges:")
print(graph_un.edges())
print("------------------------------")
print("duplicates:")
print(duplicates)
print("------------------------------")
print("heights:")
print(heights)
print("------------------------------")
print("first edge")
print(first_edge)
print("------------------------------")


pos = nx.planar_layout(graph_un)

subax2 = plt.subplot(122)

nx.draw(graph_un, pos, node_color = 'r', with_labels=True)

plt.show()

graph = nx.MultiGraph(graph_un)  

for dup in duplicates:
    graph.add_edge(dup[0], dup[1])

print(graph.edges())

medial_graph = SignedPlanarGraph()

medial_graph.create_nodes_from_faces(graph)

medial_graph.create_edges_after_nodes()

medial_graph.draw_sp_graph()


