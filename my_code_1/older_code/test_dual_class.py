


import networkx as nx
from older_code.DualGraph import DualGraph
from older_code.MedialGraphBlack import MedialGraphBlack

f_graph = nx.Graph([(0,1),(2,0),(2,1),(2,3),(1,3),(1,4),(3,4)])


dual_graph = DualGraph()

dual_graph.create_dual_from_graph(f_graph)

#dual_graph.draw_dual_graph()

medial_graph = MedialGraphBlack()

medial_graph.create_medial_from_dual(dual_graph)

medial_graph.draw_medial_graph()




