import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import sys
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph



# tefoil_with_twist
# f_graph = nx.MultiGraph([(3 , 3), (3, 0), (3 ,2), (0, 2), (0, 1), (0,1), (1,2), (1,2)])

# trefoil_with_poke
f_graph = nx.MultiGraph([(0,1), (0,1), (0,2), (0,4), (1,2), (1,4), (2,3), (2,3), (3,4), (3,4)])


pos = nx.planar_layout(f_graph)

subax2 = plt.subplot(121)
nx.draw(f_graph, pos,  with_labels=True)
plt.show()


input()

sys.exit()