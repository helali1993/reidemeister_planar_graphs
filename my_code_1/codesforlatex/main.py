from SignedPlanarGraph import SignedPlanarGraph
from HardCodedKnots import HardCodedKnots
from ReidemeisterMoves import ReidemeisterMoves

hcg = HardCodedKnots(code_no=3113)

k_gauss = hcg.get_code_gauss() 

sp_graph = SignedPlanarGraph(code_gauss = k_gauss)
sp_graph.create_and_draw_sp()


reid_sp = ReidemeisterMoves.reidemeister_main(sp_graph)

reid_sp = SignedPlanarGraph(code_gauss=reid_sp.code_gauss)
reid_sp.create_and_draw_sp()

#print(reid_sp.code_gauss)