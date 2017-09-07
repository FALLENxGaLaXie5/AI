from GraphAI import SearchTree, Node, Vertex
from RomaniaGraph import graph
            
#-----------------------------------------------------------
def GraphSearch( graph, tree, search_type, goal_state ):
    
    print('-----------GraphSearch-----------', search_type)
    
    # a list for the frontier    
    frontier = list()    
    frontier.append(tree.GetRoot())
        
    while frontier:
        #-1--- remove a node from the frontier
        if (search_type == 'BFS'):
            pnode = frontier.pop(0)    # like a queue
        else:
            pnode = frontier.pop()    # like a stack, or a priority queue
            
        #-2--- mark the node's vertex as 'explored'
        pnode.GetVertex().SetExplored()
                
        #-3--- expand this vertex by iterating over its possible actions
        neighbors = pnode.GetVertex().EdgeIterator()
        for neighbor in neighbors:
            #-4--- create a search tree node for the vertex
            node = Node(neighbor[0])
            #-5--- compute f(n) depending on type of search
            F( search_type, pnode, node, neighbor );
            
            #-6--- check if the vertex is not already explored and its node not in the frontier
            if (not neighbor[0].GetExplored() and not node in frontier):    
                #-6a--- add the node to the search tree
                tree.AddChildNode(pnode,node)
                                                        
                #-6b--- check for goal if BFS or DFS                            
                if search_type in {'BFS','DFS'}:
                    if neighbor[0] == goal_state:        return node
                        
                #-6c--- put node in frontier 
                frontier.append(node)
                if(search_type == 'UCS' or search_type == 'GRD' or search_type == 'AST'):
                    frontier.sort()

#-----------------------------------------------------------
def F( search_type, pnode, node, neighbor ):
    if (search_type == 'BFS' or search_type == 'DFS'):
        node.fcost = 1
        
    elif (search_type == 'UCS'):
        node.fcost = pnode.fcost + neighbor[1]
    elif (search_type == 'GRD'):
        node.fcost = node.GetVertex().GetValue()
    elif (search_type == 'AST'):
        node.fcost = pnode.fcost + neighbor[1] + node.GetVertex().GetValue()
        
#-----------------------------------------------------------

if __name__ == '__main__':
     
    start_state = graph.GetStartVertex()    
    goal_state  = graph.GetGoalVertex()
    
    root = Node(start_state)
    root.parent = None
    
    search_tree = SearchTree(root)    
    goal_node = GraphSearch( graph, search_tree, 'UCS', goal_state )
    #goal_node.PrintParents()
    search_tree.PrintTree()
    
    
"""
Arad, sibiu, 

Arad, sibiu, RV, Pitesti, Bucharest
"""