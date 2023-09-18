import networkx as nx
import my_helpers as help



class DualGraph(nx.MultiGraph):

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
    
    def create_dual_from_knot_planar_diagram(self, knot):
        self.create_dual_from_graph(knot)
    
    
    def create_nodes_from_faces(self, graph):

        (check, graph) = nx.check_planarity(graph)

        if not check:
            raise "graph in the input argument is not planar!!!" 
        
        faces_list = []
        for node_1 in graph.nodes():
            for node_2 in graph.nodes():
                if node_2 not in graph[node_1]:
                    continue
                faces_list.append(graph.traverse_face(node_1, node_2))
        
        i = 0
        while i < len(faces_list):
            j = i + 1
            while j < len(faces_list):
                if help.is_cyclic_list(faces_list[i], faces_list[j]):
                    faces_list.remove(faces_list[j])
                    j = j - 1
                j =  j + 1
            i = i + 1
        nodes = []
        
        for i in range(len(faces_list)):
            nodes.append(str(faces_list[i]).strip("[]").replace(", ", ""))
            
        self.add_nodes_from(nodes)

    def create_edges_after_nodes(self):
        edges = []
        nodes = list(self.nodes())
        for i in range(0,len(nodes)):
            for j in range(i+1, len(nodes)):
                subsets = help.edges_set_dual_creation(nodes[i])
                for subset in subsets:
                    rev_next_node = nodes[j][::-1]
                    if help.sublistExists(subset, nodes[j]) :
                        edges.append((nodes[i], nodes[j]))
                    if help.sublistExists(subset, rev_next_node):
                        edges.append((nodes[i], nodes[j]))
                    last_edge = nodes[j][len(nodes[j])-1:] + nodes[j][:1]
                    last_edge_rev = last_edge[::-1]
                    if help.sublistExists(subset, last_edge):
                        edges.append((nodes[i], nodes[j]))
                    if help.sublistExists(subset, last_edge_rev):
                        edges.append((nodes[i], nodes[j]))
        self.add_edges_from(edges)

    def create_dual_from_graph(self, graph):
        self.create_nodes_from_faces(graph)
        self.create_edges_after_nodes()

    def draw_dual_graph(self, path=None):
        if path:
            pass
        else:
            import matplotlib.pyplot as plt
            from networkx.drawing.nx_agraph import to_agraph 
            subax = plt.subplot(121)
            pos = nx.planar_layout(self)
            A = to_agraph(self)
            path_final = "pyknotid_helali/my_code_1/images/dual_graph" + str(self.drawing_number) + ".png"
            A.draw( path_final, prog='dot')
        self.drawing_number += 1






