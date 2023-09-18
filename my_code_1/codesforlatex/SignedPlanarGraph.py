import networkx as nx
import my_helpers as help
import copy


class SignedPlanarGraph:

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

    def __eq__(self, other):

        if str(self.code_gauss) == str(other.code_gauss):
            if nx.is_isomorphic(self.black_graph, other.black_graph):
                if nx.is_isomorphic(self.white_graph, other.white_graph):
                    if self.signed_black == other.signed_black:
                        if self.signed_white == other.signed_white:
                            return True
        return False


    def __ne__(self, other):
        return not self.__eq__(other)

    def create_nodes_from_faces(self, graph):
        
        (check, planar_graph) = nx.check_planarity(graph)
        faces_first_run = SignedPlanarGraph.get_faces_list(planar_graph)
        faces = SignedPlanarGraph.add_loops_face_list(graph, faces_first_run)
        outer_face = SignedPlanarGraph.get_longest_region(faces)
        outer_regions = SignedPlanarGraph.get_outer_regions(outer_face, faces)
        [black, white] = SignedPlanarGraph.shade_faces(outer_regions, faces, outer_face)

        black_nodes = []
        for b in black:
            black_nodes.append(str(b).strip("[]").replace(", ", ""))
        self.black_graph.add_nodes_from(black_nodes)

        white_nodes = []
        for w in white:
            white_nodes.append(str(w).strip("[]").replace(", ", ""))
        self.white_graph.add_nodes_from(white_nodes)

        self.black_loops = []
        for b in self.black_graph.nodes():
            if len(b) == 2:
                if b[0] == b[1]:
                    self.black_loops.append(b)

        self.white_loops = []
        for w in self.white_graph.nodes():
            if len(w) == 2:
                if w[0] == w[1]:
                    self.white_loops.append(w)



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
            white_loops = copy.deepcopy(self.white_loops)    
            for white_loop in white_loops:
                if white_loop[0] in nodes[i]:
                    edges.append((nodes[i], nodes[i]))
                    the_last = white_loop[0]
                    the_last_index = nodes[i].find(the_last)
                    m = (the_last_index - 1) % len(nodes[i])
                    n = (the_last_index + 1) % len(nodes[i])
                    while True:
                        if nodes[i][m] == nodes[i][n]:
                            edges.append((nodes[i], nodes[i]))
                            another = the_last + "" + nodes[i][m]
                            self.white_loops.append(another)
                            m = (m - 1) % len(nodes[i])
                            n = (n  + 1) % len(nodes[i])
                            continue
                        break
            i += 1


        self.black_graph.add_edges_from(edges)

        nodes = self.white_graph.nodes()
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
            black_loops = copy.deepcopy(self.black_loops)
            for black_loop in black_loops:
                if black_loop[0] in nodes[i]:
                    edges.append((nodes[i], nodes[i]))
                    the_last = black_loop[0]
                    the_last_index = nodes[i].find(the_last)
                    m = (the_last_index - 1) % len(nodes[i])
                    n = (the_last_index + 1) % len(nodes[i])
                    while True:
                        if nodes[i][m] == nodes[i][n]:
                            edges.append((nodes[i], nodes[i]))
                            another = the_last + "" + nodes[i][m]
                            self.black_loops.append(another)
                            m = (m - 1) % len(nodes[i])
                            n = (n  + 1) % len(nodes[i])
                            continue
                        break
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
                if SignedPlanarGraph.check_same_edge_region(face, longest_region):
                    outer_regions.append(face)
                    check_if_loop = str(face).strip("[]").replace(", ", "")
                    if len(check_if_loop) == 2:
                        loops.append(face)
        for loop in loops:
            if loop[0] == loop[1]:
                continue
            for region in outer_regions:
                if loop != region:
                    if SignedPlanarGraph.check_same_edge_region(loop, region):
                        outer_regions.remove(region)
        return outer_regions

    @staticmethod
    def shade_faces(outer_reigons,faces_list, outer_face):

        black_shades = outer_reigons
        white_shades = [outer_face]

        coloured = black_shades + white_shades

        ple_faces = [str(face[0]) + str(face[1]) for face in faces_list if len(face) == 2]

        nbr_black_turn = True
        got_coloured= outer_reigons


        skipped = False
        while len(coloured) != len(faces_list):
            next_got_coloured = []
            if nbr_black_turn:
                for face in got_coloured:
                    for next_face in faces_list:
                        if next_face not in coloured:
                            if face != next_face:
                                if SignedPlanarGraph.check_same_edge_region(face, next_face):
                                    if len(next_face) > 2:
                                        [cond, edge] = SignedPlanarGraph.check_same_edge_region(face, next_face)
                                        if edge in ple_faces or edge[::-1] in ple_faces:
                                            skipped = True
                                            continue
                                    coloured.append(next_face)
                                    white_shades.append(next_face)
                                    next_got_coloured.append(next_face)
                nbr_black_turn = False
                got_coloured = next_got_coloured
            else:
                for face in got_coloured:
                    for next_face in faces_list:
                        if next_face not in coloured:
                            if face != next_face:
                                if SignedPlanarGraph.check_same_edge_region(face, next_face):
                                    if len(next_face) > 2:
                                        [cond, edge] = SignedPlanarGraph.check_same_edge_region(face, next_face)
                                        if edge in ple_faces or edge[::-1] in ple_faces:
                                            continue
                                    coloured.append(next_face)
                                    black_shades.append(next_face)
                                    next_got_coloured.append(next_face)
                nbr_black_turn = True
                got_coloured = next_got_coloured
            if skipped and len(got_coloured) == 0 and len(coloured) != len(faces_list):
                remaining = [face for face in faces_list if face not in coloured]
                for face in remaining:
                    jump = False
                    for next_face in coloured:
                        if SignedPlanarGraph.check_same_edge_region(face, next_face):
                            if next_face in black_shades:
                                white_shades.append(face)
                            elif next_face in white_shades:
                                black_shades.append(face)
                            coloured.append(face)
                            jump = True
                        if jump:
                            break    
            if  len(got_coloured) == 0 and len(coloured) != len(faces_list):
                remaining = [face for face in faces_list if face not in coloured]
                for face in remaining:
                    jump = False
                    for next_face in coloured:
                        if SignedPlanarGraph.check_same_edge_region(face, next_face):
                            if next_face in black_shades:
                                white_shades.append(face)
                            elif next_face in white_shades:
                                black_shades.append(face)
                            coloured.append(face)
                            jump = True
                        if jump:
                            break     

        return black_shades, white_shades

    @staticmethod
    def check_same_edge_region(face_1, face_2):
        face_str_1 = str(face_1).strip("[]").replace(", ", "")
        face_str_2 = str(face_2).strip("[]").replace(", ", "")
        subsets = help.edges_set_creation(face_str_1)
        for subset in subsets:
            rev_face_str_2 = face_str_2[::-1]
            if help.sublistExists(subset, face_str_2):
                return True, subset
            if help.sublistExists(subset, rev_face_str_2):
                return True, subset
            last_edge = face_str_2[len(face_str_2)-1:] + face_str_2[:1]
            rev_last_edge = last_edge[::-1]
            if help.sublistExists(subset, last_edge):
                return True, subset
            if help.sublistExists(subset, rev_last_edge):
                return True, subset
            if subset[0] == subset[1]:
                if help.sublistExists(subset[0], face_str_2):
                    return True, subset
        return False

    def draw_sp_graph(self, path=None):
            if path:
                pass
            else:
                from networkx.drawing.nx_agraph import to_agraph

                A = to_agraph(self.black_graph)
                path_final = "pyknotid_helali/my_code_1/images/medial_graph_black" + str(SignedPlanarGraph.drawing_number) + ".png"
                A.draw( path_final, prog='dot')
                SignedPlanarGraph.drawing_number += 1

                pos = nx.planar_layout(self.white_graph)
                A = to_agraph(self.white_graph)
                path_final = "pyknotid_helali/my_code_1/images/medial_graph_white" + str(SignedPlanarGraph.drawing_number) + ".png"
                A.draw( path_final, prog='dot')
                SignedPlanarGraph.drawing_number += 1


    def draw_sp_graph_sign(self, path=None):
            if path:
                pass
            else:
                from networkx.drawing.nx_agraph import to_agraph
                
                joker_graph = nx.MultiGraph()
                joker_signs = copy.deepcopy(self.signed_black)

    
                for sign in joker_signs:
                    joker_graph.add_edge(sign[0][0],sign[0][1], label = sign[1])


                A = to_agraph(joker_graph)
                path_final = "pyknotid_helali/my_code_1/images/medial_graph_black" + str(SignedPlanarGraph.drawing_number) + ".png"
                A.draw( path_final, prog='dot')
                SignedPlanarGraph.drawing_number += 1

                joker_graph = nx.MultiGraph()
                joker_signs = copy.deepcopy(self.signed_white)

                for sign in joker_signs:
                    joker_graph.add_edge(sign[0][0],sign[0][1], label = sign[1])
                
                A = to_agraph(joker_graph)
                path_final = "pyknotid_helali/my_code_1/images/medial_graph_white" + str(SignedPlanarGraph.drawing_number) + ".png"
                A.draw( path_final, prog='dot')
                SignedPlanarGraph.drawing_number += 1


   
    def sign_sp(self):
        if self.code_gauss:
            code_gauss_splitted = str(self.code_gauss).split(",")

            black_loops = copy.deepcopy(self.black_loops)
            white_loops = copy.deepcopy(self.white_loops)

            already_signed_black = []
            for b_edge in self.black_graph.edges():
                if b_edge in already_signed_black:
                    if b_edge[0] != b_edge[1]:
                        continue
                already_signed_black.append(b_edge)
                remove_brackets = str(b_edge).strip("()").replace("'", "")
                nodes = remove_brackets.split(", ")
                shift = False
                if nodes[0] != nodes[1]:
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

                            if len(edges[0]) == 2 and edges[0][0] == edges[0][1]:
                                shift = True
                            if len(edges[1]) == 2 and edges[1][0] == edges[1][1]:
                                shift = True

                            faces= list(self.black_graph.nodes()) + list(self.white_graph.nodes())
                            the_face = help.get_bounded_face(edges, faces)
                            if the_face is not None:
                                if the_face in self.black_graph.nodes():
                                    if the_gc[2] == "a":
                                        if not shift:
                                            self.signed_black.append((b_edge, "+", char))
                                        else:
                                            self.signed_black.append((b_edge, "-", char))
                                    elif the_gc[2] == "c":
                                        if not shift:
                                            self.signed_black.append((b_edge, "-", char))
                                        else:
                                            self.signed_black.append((b_edge, "+", char))
                                elif the_face in self.white_graph.nodes():
                                    if the_gc[2] == "a":
                                        if not shift:
                                            self.signed_black.append((b_edge, "-", char) )
                                        else:
                                            self.signed_black.append((b_edge, "+", char) )
                                    elif the_gc[2] == "c":
                                        if not shift:
                                            self.signed_black.append((b_edge, "+", char))
                                        else:
                                            self.signed_black.append((b_edge, "-", char))

                elif nodes[0] == nodes[1]:
                    crossed_at = None
                    for white_loop in white_loops:
                        if white_loop[0] in nodes[0]:
                            crossed_at = white_loop[0]
                            white_loops.remove(white_loop)
                            break
                    if crossed_at == None:
                        raise Exception("Loop does not exsist!!! Edge is not correct!!!")
                    for gc in code_gauss_splitted:
                        if gc[0] == crossed_at:
                            if gc[2] == "a":
                                self.signed_black.append((b_edge, "+", crossed_at))
                            elif gc[2] == "c":
                                self.signed_black.append((b_edge, "-", crossed_at))
                            break

            already_signed_white = []
            for w_edge in self.white_graph.edges():
                if w_edge in already_signed_white:
                    if w_edge[0] != w_edge[1]:
                        continue
                already_signed_white.append(w_edge)
                remove_brackets = str(w_edge).strip("()").replace("'", "")
                nodes = remove_brackets.split(", ")
                shift = False
                if nodes[0] != nodes[1]:
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

                            if len(edges[0]) == 2 and edges[0][0] == edges[0][1]:
                                shift = True
                            if len(edges[1]) == 2 and edges[1][0] == edges[1][1]:
                                shift = True          
                        
                            faces= list(self.black_graph.nodes()) + list(self.white_graph.nodes())
                            the_face = help.get_bounded_face(edges, faces)
                            if the_face is not None:
                                if the_face in self.white_graph.nodes():
                                    if the_gc[2] == "a":
                                        if not shift:
                                            self.signed_white.append((w_edge, "+", char) )
                                        else:
                                            self.signed_white.append((w_edge, "-", char) )
                                    elif the_gc[2] == "c":
                                        if not shift:
                                            self.signed_white.append((w_edge, "-", char))
                                        else:
                                            self.signed_white.append((w_edge, "+", char))
                                elif the_face in self.black_graph.nodes():
                                    if the_gc[2] == "a":
                                        if not shift:
                                            self.signed_white.append((w_edge, "-", char) )
                                        else:
                                            self.signed_white.append((w_edge, "+", char) )
                                    elif the_gc[2] == "c":
                                        if not shift:
                                            self.signed_white.append((w_edge, "+", char))
                                        else:
                                            self.signed_white.append((w_edge, "-", char))
                elif nodes[0] == nodes[1]:
                    crossed_at = None
                    for black_loop in black_loops:
                        if black_loop[0] in nodes[0]:
                            crossed_at = black_loop[0]
                            black_loops.remove(black_loop)
                            break
                    if crossed_at == None:
                        raise Exception("Loop does not exsist!!! Edge is not correct!!!")
                    for gc in code_gauss_splitted:
                        if gc[0] == crossed_at:
                            if gc[2] == "a":
                                self.signed_white.append((w_edge, "+", crossed_at))
                            elif gc[2] == "c":
                                self.signed_white.append((w_edge, "-", crossed_at)) 
                            break                 
           
        else:
            raise Exception("Gauss Code is Empty!!! We are flying blind!!!")

    def create_and_draw_sp(self):
        graph = help.create_planar_graph_from_gauss_code(self.code_gauss)
        self.create_nodes_from_faces(graph)
        self.create_edges_after_nodes()
        self.sign_sp()
        self.draw_sp_graph()
        self.draw_sp_graph_sign()

    def create_and_sign_sp(self):
        graph = help.create_planar_graph_from_gauss_code(self.code_gauss)
        self.create_nodes_from_faces(graph)
        self.create_edges_after_nodes()
        self.sign_sp()
        

    def label_edges_sp(Agraph, signs):
        temp_signs = copy.deepcopy(signs)
        for data in signs:  
            edge = data[0]

    def find_loops_in_sp(self):
        
        self.black_loops = []
        for b in self.black_graph.nodes():
            if len(b) == 2:
                if b[0] == b[1]:
                    self.black_loops.append(b)

        self.white_loops = []
        for w in self.white_graph.nodes():
            if len(w) == 2:
                if w[0] == w[1]:
                    self.white_loops.append(w)

    def find_cycles_of_length(graph, desired_length):
        no_multi_graph = SignedPlanarGraph.multigraph_to_graph(graph)
        cycles = nx.cycle_basis(no_multi_graph)
        cycles_of_length = [cycle for cycle in cycles if len(cycle) == desired_length]
        return cycles_of_length

    def multigraph_to_graph(multi_graph):
        graph = nx.Graph()
        for u, v, key, data in multi_graph.edges(data=True, keys=True):
            graph.add_edge(u, v)
        return graph

        


        
