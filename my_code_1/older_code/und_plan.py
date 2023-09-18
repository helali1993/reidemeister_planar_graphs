from pyknotid.catalogue import get_knot
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph

k = get_knot('4_1').space_curve()



[graph_un, duplicates, heights, first_edge]  = k.planar_diagram().as_networkx()


# print(graph_un.edges())
# print(duplicates)

pos = nx.planar_layout(graph_un)

subax2 = plt.subplot(122)

nx.draw(graph_un, pos, node_color = 'r', with_labels=True)

plt.show()

graph = nx.MultiGraph(graph_un)

for dup in duplicates:
    graph.add_edge(dup[0], dup[1])

print(graph.edges())

medial_graph = SignedPlanarGraph(code_gauss=k.gauss_code())
medial_graph.create_and_draw_sp(graph)

# medial_graph.create_nodes_from_faces(graph)

print("Black Nodes:")
print(medial_graph.black_graph.nodes())
print("===================================")
print("White Nodes:")
print(medial_graph.white_graph.nodes())
print("===================================")
# medial_graph.create_edges_after_nodes()

print("Black Edges:")
print(medial_graph.black_graph.edges())
print("===================================")
print("White Edges:")
print(medial_graph.white_graph.edges())
print("===================================")
print(k.gauss_code())
print("===================================")
print(medial_graph.signed_black)
print("===================================")
print(medial_graph.signed_white)



























# medial_graph.draw_medial_graph()


# print("Dataaaaaaaaaaaaaaaaa")
# print(faces)
# print(outer_face)

# print("Testing first shading")
# first_shade = medial_graph.get_outer_regions(outer_face, faces)
# print(first_shade)

# print("Testing shading")
# [black, white] = MedialGraph.shade_faces(first_shade, faces)
# print(black)
# print(white)

