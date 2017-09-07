# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:03:57 2017

@author: joshua.steward095
"""

from GraphAI import Graph, Vertex

#-----------------------------------------------------------
v = list()
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

#-----------------------------------------------------------
graph = Graph(directed=False)

for i in range (0, 20):
    graph.AddVertex(v[i])

graph.SetStartVertex(v[0])
graph.SetGoalVertex(v[1])

graph.AddEdge(v[0], v[15], 140)
graph.AddEdge(v[0], v[16], 118)
graph.AddEdge(v[0], v[19], 75)

graph.AddEdge(v[16], v[9], 111)
graph.AddEdge(v[15], v[14], 80)
graph.AddEdge(v[15], v[5], 99)
graph.AddEdge(v[19], v[12], 71)

graph.AddEdge(v[9], v[10], 70)

graph.AddEdge(v[14], v[2], 146)
graph.AddEdge(v[14], v[13], 97)

graph.AddEdge(v[5], v[1], 211)
 
graph.AddEdge(v[12], v[15], 151)

graph.AddEdge(v[10], v[3], 75)

graph.AddEdge(v[3], v[2], 120)

graph.AddEdge(v[2], v[13], 138)

graph.AddEdge(v[13], v[1], 101)