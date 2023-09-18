from SignedPlanarGraph import SignedPlanarGraph
import copy
import networkx as nx
import my_helpers as help

class ReidemeisterMoves:


    def reidemeister_main(sp_graph: SignedPlanarGraph) -> SignedPlanarGraph:

        reid_I, reid_II, reid_III = True, True, True
        joker_sp = copy.deepcopy(sp_graph)

        while reid_I or reid_II or reid_III:
            if reid_I or reid_II or reid_III:
                joker_sp_reid_I = ReidemeisterMoves.reidemeister_I(joker_sp)
                if joker_sp != joker_sp_reid_I:
                    joker_sp = joker_sp_reid_I
                    reid_I = False
                    reid_II, reid_III = True, True
                else:
                    reid_I = False
        
            if reid_I or reid_II or reid_III:
                joker_sp_reid_II = ReidemeisterMoves.reidemeister_II(joker_sp)
                if joker_sp != joker_sp_reid_II:
                    joker_sp = joker_sp_reid_II
                    reid_II = False
                    reid_I, reid_III = True, True
                else:
                    reid_II = False

            if reid_I or reid_II or reid_III:
                joker_sp_III = ReidemeisterMoves.reidemeister_III(joker_sp)
                if joker_sp != joker_sp_III:
                    joker_sp = joker_sp_III
                    reid_III = False
                    reid_I, reid_II = True, True
                else:
                    reid_III = False

        joker_sp = SignedPlanarGraph(code_gauss = joker_sp.code_gauss)
        joker_sp.create_and_sign_sp()
        return joker_sp

    def reidemeister_I(sp_graph: SignedPlanarGraph) -> SignedPlanarGraph:
        
        reid_I = copy.deepcopy(sp_graph)
        while True:
            reid_I_new = ReidemeisterMoves.reidemeister_I_helper(reid_I)
            if reid_I == reid_I_new:
                return reid_I_new
            reid_I = reid_I_new

    def reidemeister_II(sp_graph: SignedPlanarGraph) -> SignedPlanarGraph:
        reid_II = copy.deepcopy(sp_graph)
        while True:
            reid_II_new = ReidemeisterMoves.reidemeister_II_helper(reid_II)
            if reid_II_new == reid_II:
                return reid_II_new
            reid_II = reid_II_new

    def reidemeister_III(sp_graph: SignedPlanarGraph) -> SignedPlanarGraph:
        reid_III = copy.deepcopy(sp_graph)
        while True:
            reid_III_new = ReidemeisterMoves.reidemeister_III_helper(reid_III)
            if reid_III_new == reid_III:
                return reid_III_new
            reid_III = reid_III_new

    def reidemeister_I_helper(sp_graph: SignedPlanarGraph) -> SignedPlanarGraph:
        '''
        we start by checking if the black graph has loops
        '''
        if sp_graph.white_loops != None:
            sp_graph.find_loops_in_sp()
            if len(sp_graph.white_loops) != 0:
                white_loops = copy.deepcopy(sp_graph.white_loops)
                for white_loop in white_loops:
                    crossing = white_loop[0]
                    for edge in sp_graph.black_graph.edges():
                        if edge[0] == edge[1]:
                            if crossing in edge[0]:
                                for signed_edge in sp_graph.signed_black:
                                    if signed_edge[0] == edge:
                                        sign = signed_edge[1]
                                        for w_node in sp_graph.white_graph.nodes():
                                            if len(w_node) == 2:
                                                if w_node[0] == w_node[1]:
                                                    if crossing in w_node:
                                                        if len(sp_graph.white_graph[w_node]) == 1:
                                                            for signed_opp_edge in sp_graph.signed_white:
                                                                if w_node in signed_opp_edge[0]:
                                                                    sign_opp = signed_opp_edge[1]
                                                                    if sign != sign_opp:
                                                                        '''
                                                                        We have found an RI pair!!!
                                                                        '''

                                                                        '''
                                                                        This part is not needed
                                                                        '''
                                                                        joker_sp = copy.deepcopy(sp_graph)
                                                                        joker_sp.black_graph.remove_edge(edge[0], edge[1])
                                                                        joker_sp.signed_black.remove(signed_edge)
                                                                        for n_node in sp_graph.white_graph[w_node]:
                                                                            pass
                                                                        joker_sp.white_graph.remove_edge(w_node, n_node)
                                                                        joker_sp.signed_white.remove(signed_opp_edge)

                                                                        '''
                                                                        Cleaning up
                                                                        '''

                                                                        code_gauss_final = copy.deepcopy(joker_sp.code_gauss)
                                                                        code_gauss_final = str(code_gauss_final)
                                                                        code_gauss_final_splitted = code_gauss_final.split(",")

                                                                        code_gauss_final = []
                                                                        for code in code_gauss_final_splitted:
                                                                            if crossing not in code:
                                                                                code_gauss_final += code + ","

                                                                        code_gauss_final = code_gauss_final[ : len(code_gauss_final) - 1]
                                                                        code_gauss_final = ''.join(code_gauss_final)

                                                                        final_sp = SignedPlanarGraph(code_gauss= code_gauss_final)
                                                                        final_sp.create_and_sign_sp()
                                                                        return final_sp
        if sp_graph.black_loops != None:
            sp_graph.find_loops_in_sp()
            if len(sp_graph.black_loops) != 0:
                black_loops = copy.deepcopy(sp_graph.black_loops)
                for black_loop in black_loops:
                    crossing = black_loop[0]
                    for edge in sp_graph.white_graph.edges():
                        if edge[0] == edge[1]:
                            if crossing in edge[0]:
                                for signed_edge in sp_graph.signed_white:
                                    if signed_edge[0] == edge:
                                        sign = signed_edge[1]
                                        for b_node in sp_graph.black_graph.nodes():
                                            if len(b_node) == 2:
                                                if b_node[0] == b_node[1]:
                                                    if crossing in b_node:
                                                        if len(sp_graph.black_graph[b_node]) == 1:
                                                            for signed_opp_edge in sp_graph.signed_black:
                                                                if b_node in signed_opp_edge[0]:
                                                                    sign_opp = signed_opp_edge[1]
                                                                    if sign != sign_opp:
                                                                        '''
                                                                        We have found an RI pair!!!
                                                                        '''
                                                                        joker_sp = copy.deepcopy(sp_graph)

                                                                        '''
                                                                        Cleaning up
                                                                        '''

                                                                        code_gauss_final = copy.deepcopy(joker_sp.code_gauss)
                                                                        code_gauss_final = str(code_gauss_final)
                                                                        code_gauss_final_splitted = code_gauss_final.split(",")

                                                                        code_gauss_final = ""
                                                                        for code in code_gauss_final_splitted:
                                                                            if crossing not in code:
                                                                                code_gauss_final += code + ","

                                                                        code_gauss_final = code_gauss_final[ : len(code_gauss_final) - 1]
                                                                        code_gauss_final = ''.join(code_gauss_final)

                                                                        final_sp = SignedPlanarGraph(code_gauss= code_gauss_final)
                                                                        final_sp.create_and_sign_sp()
                                                                        return final_sp                                          
        return sp_graph

    def reidemeister_II_helper(sp_graph: SignedPlanarGraph) -> SignedPlanarGraph:
        
        black_reid = ReidemeisterMoves.reidemeister_II_helper_black(sp_graph)
        if black_reid is not None:
            return black_reid
        
        white_reid = ReidemeisterMoves.reidemeister_II_helper_white(sp_graph)
        if white_reid is not None:
            return white_reid
        
        return sp_graph


    def reidemeister_II_helper_black(sp_graph: SignedPlanarGraph) -> SignedPlanarGraph:    
        '''
        We start by checking parrallel edges in the black graph.
        and keeping note of their different signs
        '''
        duplicates = {}
        signs = {}
        found_parrallel = False
        for edge in sp_graph.signed_black:
            if edge[0] in duplicates:
                duplicates[edge[0]] += 1
                signs[edge[0]] += edge[1]
                found_parrallel = True
            else:
                duplicates[edge[0]] = 1
                signs[edge[0]] = edge[1]

        # Parrallel Edges exist
        if found_parrallel:
            # We filter the edges from the dictionaries, 
            # to only have edges that have count more than 1.
            filtered_duplicates = {edge: count for edge, count in duplicates.items() if count >= 2}
            filtered_signs = {edge: sign for edge, sign in signs.items() if edge in filtered_duplicates}

            for edge in filtered_duplicates:
                sign = filtered_signs[edge]
                # Skip parrallel edges with only one type of sign.
                if len(set(sign)) == 1:
                    continue
                
                
                parrallel_edges = []
                for signed_edge in sp_graph.signed_black:
                    if signed_edge[0] == edge:
                        parrallel_edges.append(signed_edge)
                    i = 0
                    while i < len(parrallel_edges):
                        j = i + 1
                        break_outer = False
                        face = ""
                        while j < len(parrallel_edges):
                            pe_1 = parrallel_edges[i]
                            pe_2 = parrallel_edges[j]
                            if pe_1[1] != pe_2[1]:
                                face = pe_1[2] + pe_2[2]
                                if face in sp_graph.white_graph.nodes():
                                    face_edges = []
                                    for w_edge in sp_graph.signed_white:
                                        if face in w_edge[0]:
                                            face_edges.append(w_edge)
                                    if len(face_edges) == 2:
                                        if face_edges[0][1] != face_edges[1][1]:
                                            break_outer = True
                                            break
                                if face[::-1] in sp_graph.white_graph.nodes():
                                    face = face[::-1] 
                                    face_edges = []
                                    for w_edge in sp_graph.signed_white:
                                        if face in w_edge[0]:
                                            face_edges.append(w_edge)
                                    if len(face_edges) == 2:
                                        if face_edges[0][1] != face_edges[1][1]:
                                            break_outer = True
                                            break
                            j += 1
                        if break_outer:
                            break
                        i += 1
                
                if face is None:
                    raise Exception("Something is wrong!!")
                if len(face) == 0:
                    raise Exception("Something is wrong!!")

                '''
                Cleaning up
                '''

                code_gauss_final = copy.deepcopy(sp_graph.code_gauss)
                code_gauss_final = str(code_gauss_final)
                code_gauss_final_splitted = code_gauss_final.split(",")

                code_gauss_final = []
                for code in code_gauss_final_splitted:
                    if face[0] not in code and face[1] not in code:
                        code_gauss_final += code + ","

                code_gauss_final = code_gauss_final[ : len(code_gauss_final) - 1]
                code_gauss_final = ''.join(code_gauss_final)

                final_sp = SignedPlanarGraph(code_gauss= code_gauss_final)
                final_sp.create_and_sign_sp()
                return final_sp
        return None

    def reidemeister_II_helper_white(sp_graph: SignedPlanarGraph) -> SignedPlanarGraph:    
        '''
        We start by checking parrallel edges in the black graph.
        and keeping note of their different signs
        '''
        duplicates = {}
        signs = {}
        found_parrallel = False
        for edge in sp_graph.signed_white:
            if edge[0] in duplicates:
                duplicates[edge[0]] += 1
                signs[edge[0]] += edge[1]
                found_parrallel = True
            else:
                duplicates[edge[0]] = 1
                signs[edge[0]] = edge[1]

        # Parrallel Edges exist
        if found_parrallel:
            # We filter the edges from the dictionaries, to only have edges that have count more than 1.
            filtered_duplicates = {edge: count for edge, count in duplicates.items() if count >= 2}
            filtered_signs = {edge: sign for edge, sign in signs.items() if edge in filtered_duplicates}

            for edge in filtered_duplicates:
                sign = filtered_signs[edge]
                # Skip parrallel edges with only one type of sign.
                if len(set(sign)) == 1:
                    continue
                
                
                parrallel_edges = []
                for signed_edge in sp_graph.signed_white:
                    if signed_edge[0] == edge:
                        parrallel_edges.append(signed_edge)
                i = 0
                while i < len(parrallel_edges):
                    j = i + 1
                    break_outer = False
                    face = ""
                    while j < len(parrallel_edges):
                        pe_1 = parrallel_edges[i]
                        pe_2 = parrallel_edges[j]
                        if pe_1[1] != pe_2[1]:
                            face = pe_1[2] + pe_2[2]
                            if face in sp_graph.black_graph.nodes():
                                face_edges = []
                                for b_edge in sp_graph.signed_black:
                                    if face in b_edge[0]:
                                        face_edges.append(b_edge)
                                if len(face_edges) == 2:
                                    if face_edges[0][1] != face_edges[1][1]:
                                        break_outer = True
                                        break
                            if face[::-1] in sp_graph.black_graph.nodes():
                                face = face[::-1] 
                                face_edges = []
                                for b_edge in sp_graph.signed_black:
                                    if face in b_edge[0]:
                                        face_edges.append(b_edge)
                                if len(face_edges) == 2:
                                    if face_edges[0][1] != face_edges[1][1]:
                                        break_outer = True
                                        break
                        j += 1
                    if break_outer:
                        break
                    i += 1
                
                if face is None:
                    raise Exception("Something is wrong!!")
                if len(face) == 0:
                    raise Exception("Something is wrong!!")

                '''
                Cleaning up
                '''

                code_gauss_final = copy.deepcopy(sp_graph.code_gauss)
                code_gauss_final = str(code_gauss_final)
                code_gauss_final_splitted = code_gauss_final.split(",")

                code_gauss_final = []
                for code in code_gauss_final_splitted:
                    if face[0] not in code and face[1] not in code:
                        code_gauss_final += code + ","

                code_gauss_final = code_gauss_final[ : len(code_gauss_final) - 1]
                code_gauss_final = ''.join(code_gauss_final)

                final_sp = SignedPlanarGraph(code_gauss= code_gauss_final)
                final_sp.create_and_sign_sp()
                return final_sp
        return None

    def reidemeister_III_helper(sp_graph:SignedPlanarGraph) -> SignedPlanarGraph:
        to_remove_gc_wh = ReidemeisterMoves.reidemeister_III_helper_white(sp_graph)
        if len(to_remove_gc_wh) != 0:
                code_gauss_final = copy.deepcopy(sp_graph.code_gauss)
                code_gauss_final = str(code_gauss_final)
                code_gauss_final_splitted = code_gauss_final.split(",")

                code_gauss_final = []
                for code in code_gauss_final_splitted:
                    if code[0] not in to_remove_gc_wh:
                        code_gauss_final += code + ","

                code_gauss_final = code_gauss_final[ : len(code_gauss_final) - 1]
                code_gauss_final = ''.join(code_gauss_final)

                final_sp = SignedPlanarGraph(code_gauss= code_gauss_final)
                final_sp.create_and_sign_sp()
                return final_sp

        to_remove_gc_bl = ReidemeisterMoves.reidemeister_III_helper_black(sp_graph)
        if len(to_remove_gc_bl) != 0:
                code_gauss_final = copy.deepcopy(sp_graph.code_gauss)
                code_gauss_final = str(code_gauss_final)
                code_gauss_final_splitted = code_gauss_final.split(",")

                code_gauss_final = []
                for code in code_gauss_final_splitted:
                    if code[0] not in to_remove_gc_bl:
                        code_gauss_final += code + ","

                code_gauss_final = code_gauss_final[ : len(code_gauss_final) - 1]
                code_gauss_final = ''.join(code_gauss_final)

                final_sp = SignedPlanarGraph(code_gauss= code_gauss_final)
                final_sp.create_and_sign_sp()
                return final_sp

        return sp_graph

    def reidemeister_III_helper_black(sp_graph:SignedPlanarGraph) -> SignedPlanarGraph:
        black_cycles = ReidemeisterMoves.reidemeister_III_find_cycles(sp_graph, "black")
        white_stars = []
        
        for bl_cycle in black_cycles:
            found = False
            opp_face = bl_cycle[1][0]
            for white_face in sp_graph.white_graph.nodes():
                if help.is_subset_both_ways(white_face, opp_face):
                    opp_face = white_face
                    found = True
                    break 
            if not found:
                continue
            faces_to_consider = []
            for face in bl_cycle[0]:
                if len(face) < 4:
                    faces_to_consider.append(face)
        
            for char in opp_face:
                if char in faces_to_consider[0] and char in faces_to_consider[1]:
                    remains = char
                    break
            faces_to_consider.append(opp_face)
            faces_to_consider_str = "".join(faces_to_consider)
            faces_to_consider_str = faces_to_consider_str.replace(char, "")
            if len(set(faces_to_consider_str)) != 4:
                continue
            return faces_to_consider_str
        return ""

    def reidemeister_III_helper_white(sp_graph:SignedPlanarGraph) -> SignedPlanarGraph:
        white_cycles = ReidemeisterMoves.reidemeister_III_find_cycles(sp_graph, "white")
        black_stars = []
        
        for wh_cycle in white_cycles:
            found = False
            opp_face = wh_cycle[1][0]
            for black_face in sp_graph.black_graph.nodes():
                if help.is_subset_both_ways(black_face, opp_face):
                    opp_face = black_face
                    found = True
                    break 
            if not found:
                continue
            faces_to_consider = []
            for face in wh_cycle[0]:
                if len(face) < 4:
                    faces_to_consider.append(face)
        
            for char in opp_face:
                if char in faces_to_consider[0] and char in faces_to_consider[1]:
                    remains = char
                    break
            faces_to_consider.append(opp_face)
            faces_to_consider_str = "".join(faces_to_consider)
            faces_to_consider_str = faces_to_consider_str.replace(char, "")
            if len(set(faces_to_consider_str)) != 4:
                continue
            return faces_to_consider_str
        return ""
        
    def reidemeister_III_find_cycles(sp_graph:SignedPlanarGraph, colour) -> list:
        if colour == "black":
            return ReidemeisterMoves.reidemeister_III_find_cycles_black(sp_graph)
        elif colour == "white":
            return ReidemeisterMoves.reidemeister_III_find_cycles_white(sp_graph)

    def reidemeister_III_find_cycles_black(sp_graph:SignedPlanarGraph):
        # We start by looking for cycles in the black graph
        black_cycles = SignedPlanarGraph.find_cycles_of_length(sp_graph.black_graph, 3)
        filtered_bl_cycles = []
        #we check the cycles to pick only with edges of different signs.
        for cycle in black_cycles:
            i = 0
            edges_sign_crossing = []
            while i < len(cycle):
                j = (i+1) % len(cycle)
                edges_sign_crossing += [(sgn_edge[1], sgn_edge[2]) for sgn_edge in sp_graph.signed_black 
                        if sgn_edge[0] == (cycle[i], cycle[j]) or sgn_edge[0] == (cycle[j],cycle[i])]
                i += 1
            crossings = []
            signs = []    
            for sgn_edge in edges_sign_crossing:
                signs.append(sgn_edge[0])
                crossings.append(sgn_edge[1])
    
            cycle_data = ("".join(crossings), "".join(signs))
            
                
            if len(set(cycle_data[1])) > 1:
                filtered_bl_cycles.append((cycle, cycle_data))
        
        return filtered_bl_cycles

    def reidemeister_III_find_cycles_white(sp_graph:SignedPlanarGraph):
        # We start by looking for cycles in the black graph
        white_cycles = SignedPlanarGraph.find_cycles_of_length(sp_graph.white_graph, 3)
        filtered_wh_cycles = []
        #we check the cycles to pick only with edges of different signs.
        for cycle in white_cycles:
            i = 0
            edges_sign_crossing = []
            # Issue if there are parrallel edges
            while i < len(cycle):
                j = (i+1) % len(cycle)
                edges_sign_crossing += [(sgn_edge[1], sgn_edge[2]) for sgn_edge in sp_graph.signed_white 
                        if sgn_edge[0] == (cycle[i], cycle[j]) or sgn_edge[0] == (cycle[j],cycle[i])]
                i += 1
            
            crossings = []
            signs = []
            for sgn_edge in edges_sign_crossing:
                signs.append(sgn_edge[0])
                crossings.append(sgn_edge[1])

            cycle_data = ("".join(crossings), "".join(signs))
                
            if len(cycle_data[1]) == 3 and len(set(cycle_data[1])) > 1:
                filtered_wh_cycles.append((cycle, cycle_data))
            
        return filtered_wh_cycles







            