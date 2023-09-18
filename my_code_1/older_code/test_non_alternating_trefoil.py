import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import sys
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph
import pyknotid.representations as rep_

k_gauss = "0-c,1+c,3-c,4-a,2-c,0+c,4+a,3+c,1-c,2+c"

planar_graph = help.create_planar_graph_from_gauss_code(k_gauss)

medial_graph = SignedPlanarGraph(code_gauss = k_gauss)
medial_graph.create_and_draw_sp(planar_graph)


# (check, planar_graph) = nx.check_planarity(f_graph)

# print(planar_graph.traverse_face(3,1))




