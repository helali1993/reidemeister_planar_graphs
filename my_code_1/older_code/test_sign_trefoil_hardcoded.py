import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import sys
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph
import pyknotid.representations as rep_

f_graph = nx.MultiGraph([(0,1),(0,1),(0,2),(0,2),(1,2),(1,2)])

str_gc = "0+c,1-c,2+c,0-c,1+c,2-c"
gc = rep_.GaussCode(str_gc)

rep = rep_.Representation(gc)

k = rep.space_curve(bool=False)
print(k.identify())

medial_graph = SignedPlanarGraph(code_gauss=gc)
medial_graph.create_and_draw_sp(f_graph)


