# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Code updated by pkodali1@asu.edu

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
w = Directions.WEST
e = Directions.EAST
n = Directions.NORTH
s = Directions.SOUTH


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    dfs_stack = util.Stack()    # Using stack for DFS
    start_node = problem.getStartState()
    visited_nodes = list()      # to keep track of the visited states
    dfs_stack.push((start_node, []))
    while True:
        curr = dfs_stack.pop()
        if problem.isGoalState(curr[0]):
            path = curr[1]
            break
        else:
            if curr[0] not in visited_nodes:
                visited_nodes.append(curr[0])
                children = problem.getSuccessors(curr[0])
                for child in children:
                    if child[0] not in visited_nodes:
                        new_path = curr[1] + [child[1]]
                        new_node = (child[0], new_path)
                        dfs_stack.push(new_node)
    return path
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    bfs_queue = util.Queue()  # Queue for BFS implementation
    start_node = problem.getStartState()
    visited_nodes = list()
    bfs_queue.push((start_node, []))
    while True:
        curr = bfs_queue.pop()
        if problem.isGoalState(curr[0]):
            path = curr[1]
            break
        else:
            if curr[0] not in visited_nodes:
                visited_nodes.append(curr[0])
                children = problem.getSuccessors(curr[0])
                for child in children:
                    if child[0] not in visited_nodes:
                        new_path = curr[1] + [child[1]]
                        new_node = (child[0], new_path)
                        bfs_queue.push(new_node)
    return path
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ucs_prioQueue = util.PriorityQueue()
    visited_nodes = list()
    path = []
    start_node = problem.getStartState()
    start_state = (start_node, path, 0)
    ucs_prioQueue.push(start_state, 0)
    while True:
        curr = ucs_prioQueue.pop()
        if problem.isGoalState(curr[0]):
            result_path = curr[1]
            break
        else:
            if curr[0] not in visited_nodes:
                visited_nodes.append(curr[0])
                children = problem.getSuccessors(curr[0])
                for child in children:
                    if child[0] not in visited_nodes:
                        new_path = curr[1] + [child[1]]
                        path_cost = curr[2] + child[2]
                        new_node = (child[0], new_path, path_cost)
                        ucs_prioQueue.push(new_node, path_cost)

    return result_path
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    astar_prioQueue = util.PriorityQueue()
    visited_nodes = list()
    path = []
    start_node = problem.getStartState()
    start_state = (start_node, path, 0)
    astar_prioQueue.push(start_state, heuristic(start_node, problem))
    while True:
        curr = astar_prioQueue.pop()
        if problem.isGoalState(curr[0]):
            result_path = curr[1]
            break
        else:
            if curr[0] not in visited_nodes:
                visited_nodes.append(curr[0])  # mark the node as visited, if not in visited
                children = problem.getSuccessors(curr[0])
                for child in children:
                    if child[0] not in visited_nodes:
                        new_path = curr[1] + [child[1]]
                        path_cost = curr[2] + child[2]
                        new_node = (child[0], new_path, path_cost)
                        astar_prioQueue.push(new_node, heuristic(child[0], problem)+ path_cost)
    return result_path
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
