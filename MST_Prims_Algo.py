# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:37:54 2020

@author: Maneesh
"""

graph = [[0, 2, 0, 6, 0], 
         [2, 0, 3, 8, 5], 
         [0, 3, 0, 0, 7], 
         [6, 8, 0, 0, 9], 
         [0, 5, 7, 9, 0]] 


def start_node(graph):
    min_value = float('inf')
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] > 0 and graph[i][j] < min_value:
                min_value = graph[i][j]
                node_i = i
                node_j = j
    return node_i, node_j, min_value
              
            
S1 = [start_node(graph)[0], start_node(graph)[1]]
S2 = []
tree = [(start_node(graph)[0], start_node(graph)[1])]         

for i in range(len(graph)):
    if i not in S1:
        S2.append(i)


def min_dist(graph):
    
    least_value = float('inf')
    
    for i in range(len(S1)):
        for j in range(len(S2)):
            if graph[S1[i]][S2[j]] > 0 and graph[S1[i]][S2[j]] < least_value:
                least_value = graph[S1[i]][S2[j]]
                next_node_i = i
                next_node_j = j
    #print(S1[next_node_i], S2[next_node_j], least_value)
    tree.append((S1[next_node_i], S2[next_node_j]))
    if S1[next_node_i] not in S1:
        S1.append(S1[next_node_i])
        S2.remove(S1[next_node_i])
    else:
        S1.append(S2[next_node_j])
        S2.remove(S2[next_node_j])
    return 

#print(min_dist(graph))

def min_span_tree(graph):
    for i in range(len(graph)):
        if len(S1) != len(graph):
            min_dist(graph)
    return tree      


def prim_algo(graph):
    print('Edges', 'Weight')
    for i in range(len(min_span_tree(graph))):
        print(tree[i][0], '-', tree[i][1], '\t', graph[tree[i][0]][tree[i][1]])
    return
        

prim_algo(graph)    



