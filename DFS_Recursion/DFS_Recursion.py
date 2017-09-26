from GraphAI import SearchTree, Node

from NQueensProblem import NQueensProblem
from RomaniaProblem import RomaniaProblem


# -----------------------------------------------------------
def DFS_Recursion(problem, tree, pnode, explored):
    if problem.GoalTest(pnode.GetState()):
        return pnode
    else:
        goal_node = Node(problem.GetStartState())
        explored.add(pnode.GetLabel())

        actions = problem.Actions(pnode.GetState())

        for action in actions:
            node = Node(action.NextState())
            if (node.GetLabel() not in explored and not problem.GoalTest(goal_node.GetState())):
                tree.AddChildNode(pnode, node)
                goal_node = DFS_Recursion(problem, tree, node, explored)

        return goal_node


# -----------------------------------------------------------

if __name__ == '__main__':
    nqueens_problem = NQueensProblem()

    start_state = nqueens_problem.GetStartState()

    root = Node(start_state)
    root.parent = None

    # explored nodes
    explored = set()

    search_tree = SearchTree(root)
    goal_node = DFS_Recursion(nqueens_problem, search_tree, root, explored)
    goal_node.PrintParents()
    # search_tree.PrintTree()

    # -------------------------------------

    romania_problem = RomaniaProblem()

    start_state = romania_problem.GetStartState()

    root = Node(start_state)
    root.parent = None

    # explored nodes
    explored = set()

    search_tree = SearchTree(root)
    goal_node = DFS_Recursion(romania_problem, search_tree, root, explored)
    goal_node.PrintParents()
    # search_tree.PrintTree()s