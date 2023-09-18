'''
This is a class For the Medial Graph.
here we define it so we can create the signed planar graphs of knots.
Since there are two types of signed graphs for knots.
We start with the graph that has the outer region as white.
And we make verticies at the areas shaded black
'''
import networkx as nx
import my_helpers as help
from older_code.DualGraph import DualGraph

class MedialGraphBlack(nx.MultiGraph):
    
    drawing_number = 0

    def __init__(self, graph_data = None, knot = None):
        if graph_data:
            super().__init__(graph_data)
        else:
            super().__init__()
        if knot:
            self.knot = knot
        else:
            self.knot = None
    
    def create_medial_from_dual(self, dual_graph : DualGraph):
        self.create_nodes_medial_dual(dual_graph)
        self.create_edges_medial_dual(dual_graph)

    def create_nodes_medial_dual(self, dual_graph: DualGraph):
        dual_edges = list(dual_graph.edges())

        medial_nodes = []
        for edge in dual_edges:
            medial_nodes.append(str(edge).strip("()"))
        
        i = 0
        while i < len(medial_nodes):            
            medial_nodes[i] = medial_nodes[i].replace( "'", "")
            medial_nodes[i] = medial_nodes[i].replace( ", ", ",")
            i += 1
        self.add_nodes_from(medial_nodes)

    def create_edges_medial_dual(self, dual_graph: DualGraph):
        if not self.nodes():
            raise "Nodes have not been Initalized!!!"
        nodes = list(self.nodes())
        print(nodes)
        edges = []

        i = 0
        while i < len(nodes) - 1:
            nodes_str_i = str(nodes[i]).split(",")
            j = i + 1
            while j < len(nodes):
                node_str_j = str(nodes[j]).split(",")
                if nodes_str_i[0] in node_str_j or nodes_str_i[1] in node_str_j:
                    edges.append((nodes[i], nodes[j]))
                j += 1
            i += 1
        print(edges)
        self.add_edges_from(edges)

    def draw_medial_graph(self, path=None):
            if path:
                pass
            else:
                import matplotlib.pyplot as plt
                from networkx.drawing.nx_agraph import to_agraph 
                subax = plt.subplot(121)
                pos = nx.planar_layout(self)
                A = to_agraph(self)
                path_final = "pyknotid_helali/my_code_1/images/medial_graph" + str(self.drawing_number) + ".png"
                A.draw( path_final, prog='dot')
                self.drawing_number += 1



        