from pyknotid.catalogue import get_knot
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph

k = get_knot('8_19').space_curve()
k_gauss = k.gauss_code()

print(k_gauss)