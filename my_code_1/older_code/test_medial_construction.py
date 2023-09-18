from pyknotid.catalogue import get_knot
import networkx as nx
import pyknotid.representations as rep_
import pyknotid.make as mk
import matplotlib.pyplot as plt
from older_code.DualGraph import DualGraph
from older_code.MedialGraphBlack import MedialGraphBlack

k = get_knot('4_1').space_curve()


[graph_un, duplicates, heights, first_edge]  = k.planar_diagram().as_networkx()

graph = nx.MultiGraph()




pos = nx.planar_layout(graph)
(check, graph_un) = nx.check_planarity(graph_un)

subax1 = plt.subplot(121)

nx.draw(graph, with_labels=True)

dual_graph = DualGraph()

# dual_graph.create_dual_from_graph(graph)

# dual_graph.draw_dual_graph()

# medial_graph = MedialGraphBlack()

# medial_graph.create_medial_from_dual(dual_graph)

# medial_graph.draw_medial_graph()

plt.show()






