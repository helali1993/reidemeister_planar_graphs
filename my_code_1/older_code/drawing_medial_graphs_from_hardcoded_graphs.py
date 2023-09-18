import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import sys
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph
import copy


f_graph = nx.MultiGraph([(0,2),(0,2),(0,1),(0,4),(1,2),(1,3),(1,3),(2,4),(3,4),(3,4)])
gauss_f_graph = "0-c,1+c,3-c,4-a,2-c,0+c,4+a,3+c,1-c,2+c"

pos = nx.planar_layout(f_graph)

subax2 = plt.subplot(121)
nx.draw(f_graph, pos,  with_labels=True)
# plt.show()

medial_graph = SignedPlanarGraph(code_gauss=gauss_f_graph)

medial_graph.create_and_draw_sp(f_graph)


print("White Data")
print(medial_graph.white_graph.nodes())
print(medial_graph.white_graph.edges())
print(medial_graph.signed_white)
# for e in medial_graph.white_graph.edges(keys=True):
#     print(e)
print("==================")
print("Black Data")
print(medial_graph.black_graph.nodes())
print(medial_graph.black_graph.edges())
print(medial_graph.signed_black)
# for e in medial_graph.black_graph.edges(keys=True):
#     print(e)
print("========================")


# subax = plt.subplot(121)
                
# pos = nx.planar_layout(medial_graph.black_graph)
# A = to_agraph(medial_graph.black_graph)
# temp_signs = copy.deepcopy(medial_graph.signed_black)

# # print(type(A.edges()))
# for e in A.edges():
#     e.attr

# # for data in temp_signs:
# #     pass


# path_final = "pyknotid_helali/my_code_1/images/medial_graph_black_testinnnnng.png"
# A.draw( path_final, prog='dot')





