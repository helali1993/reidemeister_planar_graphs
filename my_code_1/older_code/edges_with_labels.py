import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph


graph =  nx.MultiGraph()

edge = (1,2)
ll= "+"

graph.add_edge(edge[0],edge[1], label=ll)
graph.add_edge(edge[1], 0, label="_")
graph.add_edge(edge[0],edge[1], label=ll)

print(graph.edges())

A = to_agraph(graph)
path_final = "pyknotid_helali/my_code_1/images/medial_graph_black_testtttttttt.png"
A.draw( path_final, prog='dot')
