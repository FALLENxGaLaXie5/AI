from GraphAI import Graph, Vertex

#-----------------------------------------------------------
class Action(object):
    def __init__(self, w=1, ns=None):
        self.action_cost = w
        self.next_state = ns
    def ActionCost(self):        return self.action_cost
    def NextState(self):            return self.next_state


class State(object):
    def __init__( self, v=None ):
        self.vertex = v
        if v != None:
            self.label = v.label
            self.value = v.value
        else:
            self.label = "shit"
            self.value = 0
    def __eq__(self, other):
        return self.label == other.label
    def __gt__(self, other):
        return self.value > other.value
    def SetLabel(self, label):    self.label = label
    def GetLabel(self):            return self.label
    def SetValue(self, value):    self.value = value
    def GetValue(self):            return self.value



#-----------------------------------------------------------
class RomaniaProblem(object):
    def __init__(self, filename=None):
        self.graph = CreateGraph(filename)
        self.start_state = State(self.graph.GetStartVertex())
        self.goal_state = State(self.graph.GetGoalVertex())
    
    def Actions( self, state ):
        actions = []
        vertices = state.vertex.EdgeIterator()
        for vertex in vertices:
            actions.append(Action(vertex[1], State(vertex[0])))
        return actions
    def GoalTest( self, state ):
        return self.goal_state == state
    
    def SetStartState( self, start ):
        self.start_state = start
    def GetStartState( self ):
        return self.start_state
    def SetGoalState( self, goal ):
        self.goal_state = goal


#-----------------------------------------------------------
def CreateGraph( filename ):
    """
        print('-----------CreateGraph-----------')
        
        #-------------------------------
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
        
        #-----------------------------
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
        
        return graph
        """
    
    """
        print('-----------CreateGraph-----------')
        
        #-------------------------------
        v = list()
        v.append(Vertex('A', 366))
        v.append(Vertex('B', 0))
        v.append(Vertex('C', 160))
        v.append(Vertex('D', 242))
        v.append(Vertex('E', 161))
        v.append(Vertex('F', 176))
        v.append(Vertex('G', 77))
        v.append(Vertex('H', 151))
        v.append(Vertex('I', 226))
        v.append(Vertex('J', 244)    )
        v.append(Vertex('K', 241))
        v.append(Vertex('L', 234))
        v.append(Vertex('M', 380))
        
        
        #-----------------------------
        graph = Graph(directed=False)
        
        for i in range (0, 13):
        graph.AddVertex(v[i])
        
        graph.SetStartVertex(v[4])
        graph.SetGoalVertex(v[6])
        
        graph.AddEdge(v[4], v[9], 19)
        graph.AddEdge(v[4], v[8], 21)
        graph.AddEdge(v[4], v[5], 35)
        graph.AddEdge(v[4], v[7], 47)
        
        graph.AddEdge(v[9], v[10], 17)
        graph.AddEdge(v[9], v[8], 28)
        
        graph.AddEdge(v[10], v[11], 20)
        graph.AddEdge(v[10], v[12], 25)
        
        graph.AddEdge(v[11], v[12], 70)
        
        graph.AddEdge(v[8], v[2], 27)
        graph.AddEdge(v[8], v[3], 18)
        graph.AddEdge(v[8], v[5], 33)
        
        graph.AddEdge(v[5], v[4], 35)
        graph.AddEdge(v[5], v[8], 54)
        graph.AddEdge(v[5], v[3], 33)
        
        graph.AddEdge(v[3], v[6], 41)
        graph.AddEdge(v[3], v[5], 33)
        graph.AddEdge(v[3], v[8], 18)
        graph.AddEdge(v[3], v[2], 12)
        
        graph.AddEdge(v[2], v[0], 41)
        graph.AddEdge(v[2], v[1], 33)
        graph.AddEdge(v[2], v[3], 18)
        graph.AddEdge(v[2], v[8], 12)
        
        return graph
        """
    
    print('-----------CreateGraph-----------')
    
    #-------------------------------
    v = list()
    v.append(Vertex('A', 5))
    v.append(Vertex('C', 4))
    v.append(Vertex('E', 2))
    v.append(Vertex('F', 2))
    v.append(Vertex('G', 4))
    v.append(Vertex('I', 3))
    v.append(Vertex('J', 2))
    v.append(Vertex('K', 1))
    v.append(Vertex('M', 0))
    
    
    #-----------------------------
    graph = Graph(directed=False)
    
    for i in range (0, 9):
        graph.AddVertex(v[i])
    
    graph.SetStartVertex(v[0])
    graph.SetGoalVertex(v[8])
    
    graph.AddEdge(v[0], v[1], 1)
    
    graph.AddEdge(v[1], v[5], 3)
    graph.AddEdge(v[1], v[2], 4)
    
    graph.AddEdge(v[5], v[4], 2)
    graph.AddEdge(v[5], v[3], 4)
    
    graph.AddEdge(v[2], v[3], 2)
    graph.AddEdge(v[2], v[7], 4)
    graph.AddEdge(v[2], v[6], 2)
    
    graph.AddEdge(v[3], v[7], 1)
    
    graph.AddEdge(v[7], v[3], 1)
    graph.AddEdge(v[7], v[8], 1)
    
    return graph