import networkx as nx
import my_helpers as help
import copy
import matplotlib.pyplot as plt


class OldMedialGraph:

    drawing_number = 0

    def __init__(self, black_graph_data = None, white_graph_data = None, knot = None, 
                        code_gauss = None, signed_black = None, signed_white = None):
        if black_graph_data:
            self.black_graph = nx.MultiGraph(black_graph_data)
        else:
            self.black_graph = nx.MultiGraph()
        if white_graph_data:
            self.white_graph = nx.MultiGraph(white_graph_data)
        else:
            self.white_graph = nx.MultiGraph()
        if knot:
            self.knot = knot
        else:
            self.knot = None
        if code_gauss:
            self.code_gauss = code_gauss
        else:
            self.code_gauss = None
        if signed_black:
            self.signed_black = signed_black
        else:
            self.signed_black = []
        if signed_white:
            self.signed_white = signed_white
        else:
            self.signed_white = []


    def create_nodes_from_faces(self, graph):
        
        (check, planar_graph) = nx.check_planarity(graph)
        subax2 = plt.subplot(122)
        pos = nx.planar_layout(planar_graph)
        nx.draw(planar_graph, pos, with_labels=True)
        plt.show()
        print(planar_graph.edges())
        print("==========")
        print(graph.edges())
        faces_first_run = MedialGraph.get_faces_list(planar_graph)
        faces = MedialGraph.add_loops_face_list(graph, faces_first_run)
        outer_face = MedialGraph.get_longest_region(faces)
        outer_regions = MedialGraph.get_outer_regions(outer_face, faces)
        [black, white] = MedialGraph.shade_faces(outer_regions, faces)

        black_nodes = []
        for b in black:
            black_nodes.append(str(b).strip("[]").replace(", ", ""))
        self.black_graph.add_nodes_from(black_nodes)

        white_nodes = []
        for w in white:
            white_nodes.append(str(w).strip("[]").replace(", ", ""))
        self.white_graph.add_nodes_from(white_nodes)



    def create_edges_after_nodes(self):
        
        nodes = self.black_graph.nodes()
        nodes = list(nodes)
        edges = []

        i = 0
        while i < len(nodes):
            j = i + 1
            while j < len(nodes):
                if len(nodes[j]) == 2:
                    if nodes[j][0] == nodes[j][1]:
                        if nodes[j][0] in nodes[i]:
                            edges.append((nodes[i], nodes[j]))
                            j += 1
                            continue
                for ch in nodes[j]:
                    if ch in nodes[i]:
                        edges.append((nodes[i], nodes[j]))
                j +=1
            i += 1

        self.black_graph.add_edges_from(edges)

        nodes = self.white_graph.nodes()
        nodes = list(nodes)
        edges = []

        i = 0
        while i < len(nodes):
            j = i + 1
            while j < len(nodes):
                for ch in nodes[j]:
                    if ch in nodes[i]:
                        edges.append((nodes[i], nodes[j]))
                j +=1
            i += 1

        self.white_graph.add_edges_from(edges)

    @staticmethod
    def get_faces_list(planar_graph):
        graph = planar_graph
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
        return faces_list

    @staticmethod
    def get_longest_region(faces_list):
        no_edges_in_each_face = []

        for face in faces_list:
            no_edges_in_each_face.append(len(face))
        
        outer_region_index = no_edges_in_each_face.index(max(no_edges_in_each_face))
        return faces_list[outer_region_index]

    
    #Add loops as faces
    @staticmethod
    def add_loops_face_list(orig_graph, faces_list):
        graph = orig_graph
        edges = graph.edges()
        edges_list = list(edges)
        edge_count = {}
        for e in edges:
            e_str = str(e).strip("()").replace(", ", "")
            e_str = e_str.replace("'", "")
            rev_e_str = e_str[::-1]
            if e_str not in edge_count and rev_e_str not in edge_count:
                edge_count[e_str] = 1
                if e_str[0] == e_str[1]:
                    edge_count[e_str] += 1
            elif e_str in edge_count:
                edge_count[e_str] += 1
            else:
                edge_count[rev_e_str] += 1
        for e in edge_count:
            if edge_count[e] > 1:
                face = [int(e[0:1]), int(e[1:])]
                for i in range(0, edge_count[e] - 1):
                    faces_list.append(face)
        return faces_list

    @staticmethod
    def get_outer_regions(longest_region, faces_list):
    
        outer_regions = []
        loops = []

        for face in faces_list:
            if face != longest_region:
                if MedialGraph.check_same_edge_region(face, longest_region):
                    outer_regions.append(face)
                    check_if_loop = str(face).strip("[]").replace(", ", "")
                    if len(check_if_loop) == 2:
                        loops.append(face)
        for loop in loops:
            if loop[0] == loop[1]:
                continue
            for region in outer_regions:
                if loop != region:
                    if MedialGraph.check_same_edge_region(loop, region):
                        outer_regions.remove(region)
        return outer_regions



    @staticmethod
    def shade_faces(outer_regions, faces_list):
        
        faces_joker = copy.deepcopy(faces_list)
        black_shades = outer_regions
        white_shades = []

        while faces_joker:
            for face in faces_list:
                if face in black_shades:
                    for next_face in faces_list:
                        if face != next_face:
                            if next_face not in white_shades and next_face not in black_shades:
                                if MedialGraph.check_same_edge_region(face, next_face):
                                    white_shades.append(next_face)
                                    if next_face in faces_joker:
                                        faces_joker.remove(next_face)
                        if face in faces_joker:
                            faces_joker.remove(face)
                
            for face in faces_list:
                if face in white_shades:
                    for next_face in faces_list:
                        if face != next_face:
                            if next_face not in white_shades and next_face not in black_shades:
                                if MedialGraph.check_same_edge_region(face, next_face):
                                    black_shades.append(next_face)
                                    if next_face in faces_joker:
                                        faces_joker.remove(next_face)
                    if face in faces_joker:
                        faces_joker.remove(face)
        return black_shades, white_shades
            

                
    @staticmethod
    def check_same_edge_region(face_1, face_2):
        face_str_1 = str(face_1).strip("[]").replace(", ", "")
        face_str_2 = str(face_2).strip("[]").replace(", ", "")
        subsets = help.edges_set_creation(face_str_1)
        for subset in subsets:
            rev_face_str_2 = face_str_2[::-1]
            if help.sublistExists(subset, face_str_2):
                return True
            if help.sublistExists(subset, rev_face_str_2):
                return True
            last_edge = face_str_2[len(face_str_2)-1:] + face_str_2[:1]
            rev_last_edge = last_edge[::-1]
            if help.sublistExists(subset, last_edge):
                return True
            if help.sublistExists(subset, rev_last_edge):
                return True
            if subset[0] == subset[1]:
                if help.sublistExists(subset[0], face_str_2):
                    return True
        return False

    def draw_medial_graph(self, path=None):
            if path:
                pass
            else:
                import matplotlib.pyplot as plt
                from networkx.drawing.nx_agraph import to_agraph
                # I think I should change this setup a bit
                # nx.planar_layout should be check_planarity 
                # and check condition before drawing. There is 
                # also no need for plt. However I do check
                # in nodes initialization for the planar diagram of the knot.
                subax = plt.subplot(121)
                
                pos = nx.planar_layout(self.black_graph)
                A = to_agraph(self.black_graph)
                path_final = "pyknotid_helali/my_code_1/images/medial_graph_black" + str(MedialGraph.drawing_number) + ".png"
                A.draw( path_final, prog='dot')
                MedialGraph.drawing_number += 1

                pos = nx.planar_layout(self.white_graph)
                A = to_agraph(self.white_graph)
                path_final = "pyknotid_helali/my_code_1/images/medial_graph_white" + str(MedialGraph.drawing_number) + ".png"
                A.draw( path_final, prog='dot')
                MedialGraph.drawing_number += 1


    def draw_medial_graph_sign(self, path=None):
            if path:
                pass
            else:
                import matplotlib.pyplot as plt
                from networkx.drawing.nx_agraph import to_agraph
                # I think I should change this setup a bit
                # nx.planar_layout should be check_planarity 
                # and check condition before drawing. There is 
                # also no need for plt. However I do check
                # in nodes initialization for the planar diagram of the knot.

                joker_graph = nx.MultiGraph()
                joker_signs = copy.deepcopy(self.signed_black)

    
                for sign in joker_signs:
                    joker_graph.add_edge(sign[0][0],sign[0][1], label = sign[1])


                A = to_agraph(joker_graph)
                path_final = "pyknotid_helali/my_code_1/images/medial_graph_black" + str(MedialGraph.drawing_number) + ".png"
                A.draw( path_final, prog='dot')
                MedialGraph.drawing_number += 1

                joker_graph = nx.MultiGraph()
                joker_signs = copy.deepcopy(self.signed_white)

                for sign in joker_signs:
                    joker_graph.add_edge(sign[0][0],sign[0][1], label = sign[1])
                
                A = to_agraph(joker_graph)
                path_final = "pyknotid_helali/my_code_1/images/medial_graph_white" + str(MedialGraph.drawing_number) + ".png"
                A.draw( path_final, prog='dot')
                MedialGraph.drawing_number += 1


    # def sign_medial(self):
    #     if self.code_gauss:
    #         code_gauss_splitted = str(self.code_gauss).split(",")
            
    #         already_signed_black = []
    #         for b_edge in self.black_graph.edges():
    #             if b_edge in already_signed_black:
    #                 continue
    #             already_signed_black.append(b_edge)
                
    #             remove_brackets = str(b_edge).strip("()").replace("'", "")
    #             edges = remove_brackets.split(", ")
    #             for crossing in edges[0]:
    #                 if crossing in edges[1]:
    #                     for gc in code_gauss_splitted:
    #                         if crossing == gc[0]:
    #                             if gc[-1] == "a":
    #                                 self.signed_black.append((b_edge, "+"))
    #                                 break
    #                             elif gc[-1] == "c":
    #                                 self.signed_black.append((b_edge, "-"))
    #                                 break
    #                             else:
    #                                 raise Exception("Sth is up with the Gauss Code!")

    #         already_signed_white = []
    #         for w_edge in self.white_graph.edges():
    #             if w_edge in already_signed_white:
    #                 continue
    #             already_signed_white.append(w_edge)
                
    #             remove_brackets = str(w_edge).strip("()").replace("'", "")
    #             edges = remove_brackets.split(", ")
    #             for crossing in edges[0]:
    #                 if crossing in edges[1]:
    #                     for gc in code_gauss_splitted:
    #                         if crossing == gc[0]:
    #                             if gc[-1] == "a":
    #                                 self.signed_white.append((w_edge, "+"))
    #                                 break
    #                             elif gc[-1] == "c":
    #                                 self.signed_white.append((w_edge, "-"))
    #                                 break
    #                             else:
    #                                 raise Exception("Sth is up with the Gauss Code!")

    #     else:
    #         raise Exception("Gauss Code is Empty!!! We are flying blind!!!")

    def sign_medial(self):
        if self.code_gauss:
            code_gauss_splitted = str(self.code_gauss).split(",")

            already_signed_black = []
            for b_edge in self.black_graph.edges():
                if b_edge in already_signed_black:
                    continue
                already_signed_black.append(b_edge)
                remove_brackets = str(b_edge).strip("()").replace("'", "")
                nodes = remove_brackets.split(", ")
                for char in nodes[0]:
                    if char in nodes[1]:
                        code_gauss_pair = []
                        i = 0
                        while i < len(code_gauss_splitted):
                            gc = code_gauss_splitted[i]
                            if gc[0] == char:
                                the_gc = gc
                                if i == len(code_gauss_splitted) - 1:
                                    code_gauss_pair.append(code_gauss_splitted[0])
                                else:
                                    code_gauss_pair.append(code_gauss_splitted[i+1])
                            i = i + 1
                        if len(code_gauss_pair) != 2:
                            raise Exception("Either your algorithm doesn't work or the Gauss code is wrong")
                        
                        edges = []
                        edges.append(char + code_gauss_pair[0][0])
                        edges.append(char + code_gauss_pair[1][0])

                        found = False
                        faces= list(self.black_graph.nodes()) + list(self.white_graph.nodes())
                        the_face = help.get_bounded_face(edges, faces)
                        if the_face is not None:
                            if the_face in self.black_graph.nodes():
                                if the_gc[2] == "a":
                                    self.signed_black.append((b_edge, "+") )
                                elif the_gc[2] == "c":
                                    self.signed_black.append((b_edge, "-"))
                                found = True
                            elif the_face in self.white_graph.nodes():
                                if the_gc[2] == "a":
                                    self.signed_black.append((b_edge, "-") )
                                elif the_gc[2] == "c":
                                    self.signed_black.append((b_edge, "+"))
                                
            already_signed_white = []
            for w_edge in self.white_graph.edges():
                if w_edge in already_signed_white:
                    continue
                already_signed_white.append(w_edge)
                remove_brackets = str(w_edge).strip("()").replace("'", "")
                nodes = remove_brackets.split(", ")
                for char in nodes[0]:
                    if char in nodes[1]:
                        code_gauss_pair = []
                        i = 0
                        while i < len(code_gauss_splitted):
                            gc = code_gauss_splitted[i]
                            if gc[0] == char:
                                the_gc = gc
                                if i == len(code_gauss_splitted) - 1:
                                    code_gauss_pair.append(code_gauss_splitted[0])
                                else:
                                    code_gauss_pair.append(code_gauss_splitted[i+1])
                            i = i+1
                        if len(code_gauss_pair) != 2:
                            raise Exception("Either your algorithm doesn't work or the Gauss code is wrong")
                        
                        edges = []
                        edges.append(char + code_gauss_pair[0][0])
                        edges.append(char + code_gauss_pair[1][0])

                        found = False
                        for face in self.white_graph.nodes():
                            if help.edge_contained(edges[0], face):
                                if help.edge_contained(edges[1], face):
                                    if the_gc[2] == "a":
                                        self.signed_white.append((w_edge, "+") )
                                    elif the_gc[2] == "c":
                                        self.signed_white.append((w_edge, "-"))
                                    found = True
                                    break
                                
                        if not found:
                            for face in self.black_graph.nodes():
                                if help.edge_contained(edges[0], face):
                                    if help.edge_contained(edges[1], face):
                                        if the_gc[2] == "a":
                                            self.signed_white.append((w_edge, "-") )
                                        elif the_gc[2] == "c":
                                            self.signed_white.append((w_edge, "+"))
                                        break                
           
        else:
            raise Exception("Gauss Code is Empty!!! We are flying blind!!!")

    def create_and_draw_medial(self, graph):
        self.create_nodes_from_faces(graph)
        self.create_edges_after_nodes()
        self.sign_medial()
        self.draw_medial_graph()
        self.draw_medial_graph_sign()

    def label_edges_medial(Agraph, signs):
        temp_signs = copy.deepcopy(signs)
        for data in signs:
            edge = data[0]
        



        
