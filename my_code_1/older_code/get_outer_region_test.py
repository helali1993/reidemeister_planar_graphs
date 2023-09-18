import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import sys
import my_helpers as help

f_graph = nx.MultiGraph([(0,1),(0,1),(2,0),(2,1),(2,3),(2,3),(1,3),(0,3)])

pos = nx.planar_layout(f_graph)

(check, graph) = nx.check_planarity(f_graph)

for node_1 in graph.nodes():
    for node_2 in graph.nodes():
        if node_1 == node_2:
            continue
        if node_2 not in graph[node_1]:
            continue
        v = node_1
        w = node_2
        break
    break

face_nodes = []
outer_region = []
found_cycle = False

v = 2
w = 1

face_nodes = [v]
prev_node = v
cur_node = w
i = 0
    # Last half-edge is (incoming_node, v)
    #incoming_node = graph[v][w]["cw"]
while True:
    face_nodes.append(cur_node)
    if i % 2 == 0:
        prev_node, cur_node = graph.next_face_half_edge_outer(prev_node, cur_node)
        i += 1
    else:
        prev_node, cur_node = graph.next_face_half_edge_outer_cw(prev_node, cur_node)
        i += 1
    if cur_node in face_nodes:
        focus_node = cur_node
        first_index = face_nodes.index(focus_node)
        sec_index = len(face_nodes)
        while True:
            face_nodes.append(cur_node)
            if i % 2 == 0:
                prev_node, cur_node = graph.next_face_half_edge_outer(prev_node, cur_node)
                i += 1
            else:
                prev_node, cur_node = graph.next_face_half_edge_outer_cw(prev_node, cur_node)
                i += 1
            if face_nodes[first_index : sec_index] == face_nodes[sec_index: len(face_nodes)]:
                outer_region = face_nodes[first_index : sec_index]
                found_cycle = True

print(face_nodes)
print(outer_region)


        




            


