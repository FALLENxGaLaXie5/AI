from GraphAI import Vertex
from RomaniaGraph import graph
#from test_graph import graph

#-----------------------------------------------------------
def HillClimber( graph, start_vertex ):
    current_vertex = start_vertex
    while (True):
        max_vertex = Vertex(-1)
        neighbors = current_vertex.EdgeIterator()
        for neighbor in neighbors:
            if (neighbor[0] > max_vertex):
                max_vertex = neighbor[0]
        if max_vertex > current_vertex:
            current_vertex = max_vertex
            print(current_vertex.GetLabel())
        else:
            return current_vertex

#-----------------------------------------------------------

if __name__ == '__main__':
    
    start_vertex = graph.GetVertex('Fagaras')
    
    max_state = HillClimber( graph, start_vertex )
    print(max_state.GetLabel())
