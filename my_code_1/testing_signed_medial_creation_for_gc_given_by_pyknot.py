from pyknotid.catalogue import get_knot
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph
from HardCodedKnots import HardCodedKnots
from ReidemeisterMoves import ReidemeisterMoves


# k = get_knot('6_3')
# k = k.space_curve()

hcg = HardCodedKnots(code_no=5131)

k_gauss = "1+a,2-a,3+a,4-c,2+a,1-a,5+a,5-a,4+c,3-c" #hcg.get_code_gauss() # k.gauss_code()


sp_graph = SignedPlanarGraph(code_gauss = hcg.code_gauss)
sp_graph.create_and_draw_sp()
# sp_graph.create_and_sign_sp()


reid_sp = ReidemeisterMoves.reidemeister_main(sp_graph)

reid_sp = SignedPlanarGraph(code_gauss=reid_sp.code_gauss)
reid_sp.create_and_draw_sp()

print(reid_sp.code_gauss)
