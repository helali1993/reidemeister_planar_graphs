
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import sys
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph




f_graph = nx.MultiGraph([(3 , 3), (3, 0), (3 ,2), (0, 2), (0, 1), (0,1), (1,2), (1,2)])


pos = nx.planar_layout(f_graph)

subax2 = plt.subplot(121)
nx.draw(f_graph, pos,  with_labels=True)
plt.show()

# print(f_graph.edges())

medial_graph = SignedPlanarGraph()

medial_graph.create_nodes_from_faces(f_graph)

print("Black Nodes:")
print(medial_graph.black_graph.nodes())
print("White Nodes:")
print(medial_graph.white_graph.nodes())

medial_graph.create_edges_after_nodes()

print("Black Edges:")
print(medial_graph.black_graph.edges())
print("White Edges:")
print(medial_graph.white_graph.edges())

medial_graph.draw_sp_graph()

