from pyknotid.catalogue import get_knot
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import my_helpers as help
from SignedPlanarGraph import SignedPlanarGraph
from HardCodedKnots import HardCodedKnots
from ReidemeisterMoves import ReidemeisterMoves
import sys


for code_no in HardCodedKnots.code_numbers:
    
    hcg = HardCodedKnots(code_no = code_no)

    k_gauss =   hcg.get_code_gauss() 


    sp_graph = SignedPlanarGraph(code_gauss = k_gauss)
    sp_graph.create_and_draw_sp()


    reid_sp = ReidemeisterMoves.reidemeister_main(sp_graph)

    reid_sp = SignedPlanarGraph(code_gauss=reid_sp.code_gauss)
    reid_sp.create_and_draw_sp()

    print(reid_sp.code_gauss)
    input()