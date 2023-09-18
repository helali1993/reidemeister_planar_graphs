'''
This file is for methods and/or modules that will
be used across the whole project.
For easier access and better structure.
'''


import numpy as np
import collections as col
import pyknotid.representations as rep_
import networkx as nx


'''
Used to check whether two lists are equivalent w.r.t. Cyclic order.
Order is considered from left to right.
This method is mainly used to check that we do not have duplicate faces
When creating signed planar graphs.

ex 1: 
l1 = [ 1, 2 , 3] 
l2 = [3 , 1, 2]
is_cyclic_list(l1, l2) => TRUE

ex 2: 
l1 = [ 1, 2 , 3] 
l2 = [3 , 2, 1]
is_cyclic_list(l1, l2) => False
'''
def is_cyclic_list(l1, l2):
    if len(l1) != len(l2):
        return False
    if  not l1:
        return False
    elem = l1[0]
    for i in range(0,len(l1)):
        if elem == l2[i]:
            if l1 == l2[i : ] + l2[ : i]:
                return True
            return False
    return False

'''
To check if an ordered subset of list1
is contained in list2. Order is important!!
'''
def sublistExists(list1, list2):
    str_l1 = str(list1).strip("[]")
    str_l2 = str(list2).strip("[]")
    return str_l1 in str_l2

'''
used to create edges list
in order to create the edges between the nodes
in the dual graph.
'''
def edges_set_dual_creation(str_value):
    if not str_value:
        return

    edges_set = []

    for i in range(0, len(str_value) - 1):
        edges_set.append(str_value[i: i+2])
    edges_set.append(str_value[len(str_value) -1] + str_value[:1])

    return edges_set

'''
To Create all edges as stings
each edge consists of two characters
the characters represent the nodes.
'''
def edges_set_creation(str_value):
    if not str_value:
        return

    edges_set = []

    for i in range(0, len(str_value) - 1):
        edges_set.append(str_value[i: i+2])
    edges_set.append(str_value[len(str_value) -1] + str_value[:1])

    return edges_set

'''
This method is to take a Gauss Code provided from either 
The library pyknotid, or from usual conventional mathematical 
notation and modify to start counting from 0.
e.g. 1+c,2+a,.... => 0+c,1+a,...
'''

def code_gauss_from_math_to_comp(code_gauss):
    code_gauss_splitted = str(code_gauss).split(",")

    joker_code_gauss = ""

    for gc in code_gauss_splitted:
        crossing_no = int(gc[0])
        crossing_no = crossing_no - 1
        gc = str(crossing_no) + gc[1] + gc[2]
        joker_code_gauss = joker_code_gauss + gc + ","

    last_item = joker_code_gauss[len(joker_code_gauss)-1]
    if last_item == ",":
        joker_code_gauss = joker_code_gauss[:len(joker_code_gauss)-1]

    return joker_code_gauss

'''
https://stackoverflow.com/questions/48688494/python-string-search-regardless-of-character-sequence
'''

def edge_contained(substr, str):
    c1 = col.Counter(str)
    c2 = col.Counter(substr)
    return not(c2-c1)

'''
Create planar diagram from Gauss Code
'''

def create_planar_graph_from_gauss_code(code_gauss):
    
    if not code_gauss:
        raise Exception("Gauss Code is Empty")
    
    str_gc = str(code_gauss)
    code_gauss_splitted  = str_gc.split(",")

    if len(code_gauss_splitted) % 2 != 0:
        raise Exception("Gauss Code Is invalid")

    # creating a knot from the gauss code
    # to make sure that the gauss code
    # is a valid knot
    joker_gc = rep_.GaussCode(str(code_gauss))
    rep = rep_.Representation(joker_gc)
    k = rep.space_curve(bool=True)

    graph = nx.MultiGraph()

    i = 0
    while i < len(code_gauss_splitted):
        gc = code_gauss_splitted[i]
        if i == len(code_gauss_splitted) - 1:
            gc_next = code_gauss_splitted[0]
        else:
            gc_next = code_gauss_splitted[i+1]
        graph.add_edge(int(gc[0]),int(gc_next[0]))
        i+=1

    return graph

'''
To get the face that bounds the over and understrand
'''

def get_bounded_face(edges, faces):
    faces_list = []
    if len(edges[0]) == 2 and edges[0][0] == edges[0][1]:
        edges[0] = edges[0][0]
    if len(edges[1]) == 2 and edges[1][0] == edges[1][1]:
        edges[1] = edges[1][0]

    for face in faces:
        if edge_contained(edges[0], face):
            if edge_contained(edges[1], face):
                faces_list.append(face)

    if len(faces_list) == 0:
        return None
    
    no_of_edges = []
    for face in faces_list:
        no_of_edges.append(len(face))
    
    bounded_face_index = no_of_edges.index(min(no_of_edges))
    return faces_list[bounded_face_index]

def is_subset_both_ways(str_1, str_2):
    chars_1 = set(str_1)
    chars_2 = set(str_2)
    return len(str_1) == len(str_2) and chars_1.issubset(chars_2) and chars_2.issubset(chars_1)


