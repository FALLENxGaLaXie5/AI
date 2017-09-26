# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:03:57 2017

@author: joshua.steward095
"""

from GraphAI import Graph, Vertex

#-----------------------------------------------------------
v = list()
'''''
v.append(Vertex('Arad', 366))    
v.append(Vertex('Bucharest', 0))    
v.append(Vertex('Craiova', 160))    
v.append(Vertex('Dobreta', 242))    
v.append(Vertex('Eforie', 161))    
v.append(Vertex('Fagaras', 176))    
v.append(Vertex('Giurgiu', 77))
v.append(Vertex('Hirsova', 151))    
v.append(Vertex('Iasi', 226))    
v.append(Vertex('Lugoj', 244)    )
v.append(Vertex('Mehadia', 241))    
v.append(Vertex('Neamt', 234))    
v.append(Vertex('Oradea', 380))    
v.append(Vertex('Pitesti', 10))    
v.append(Vertex('RV', 193))    
v.append(Vertex('Sibiu', 253)    )
v.append(Vertex('Timisoara', 329))
v.append(Vertex('Urziceni', 80))    
v.append(Vertex('Vaslui', 199))    
v.append(Vertex('Zerind', 374))    
'''
v.append(Vertex('C1', 0))
v.append(Vertex('C2', 0))
v.append(Vertex('C3', 0))
v.append(Vertex('C4', 0))
v.append(Vertex('C5', 0))
v.append(Vertex('C6', 0))
v.append(Vertex('C7', 0))
v.append(Vertex('C8', 0))
v.append(Vertex('C9', 0))
v.append(Vertex('C10', 0))
v.append(Vertex('C11', 0))
v.append(Vertex('C12', 0))
v.append(Vertex('C13', 0))
v.append(Vertex('C14', 0))
v.append(Vertex('C15', 0))

#-----------------------------------------------------------
graph = Graph(directed=False)

for i in range (0, 15):
    graph.AddVertex(v[i])

graph.SetStartVertex(v[2])
graph.SetGoalVertex(v[14])

graph.AddEdge(v[0], v[1], 1)
graph.AddEdge(v[0], v[2], 1)

graph.AddEdge(v[1], v[3], 1)
graph.AddEdge(v[3], v[4], 1)
graph.AddEdge(v[2], v[5], 1)
graph.AddEdge(v[5], v[8], 1)
graph.AddEdge(v[8], v[9], 1)
graph.AddEdge(v[4], v[7], 1)
graph.AddEdge(v[7], v[9], 1)
graph.AddEdge(v[9], v[10], 1)
graph.AddEdge(v[4], v[6], 1)
graph.AddEdge(v[6], v[13], 1)
graph.AddEdge(v[13], v[14], 1)
graph.AddEdge(v[9], v[11], 1)
graph.AddEdge(v[11], v[12], 1)
graph.AddEdge(v[12], v[14], 1)