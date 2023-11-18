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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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
    stack = util.Stack()
    
    # Create a set to track visited states
    visited = set()
    
    # Push the initial state and an empty list of actions to the stack
    stack.push((problem.getStartState(), []))
    
    while not stack.isEmpty():
        state, actions = stack.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            for next_state, action, _ in successors:
                if next_state not in visited:
                    new_actions = actions + [action]
                    stack.push((next_state, new_actions))

    return [] 
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Create a queue for BFS
    queue = util.Queue()
    
    # Create a set to track visited states
    visited = set()
    
    # Push the initial state and an empty list of actions to the queue
    queue.push((problem.getStartState(), []))
    
    while not queue.isEmpty():
        state, actions = queue.pop()

        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            for next_state, action, _ in successors:
                if next_state not in visited:
                    new_actions = actions + [action]
                    queue.push((next_state, new_actions))

    return []  # Return an empty list if no solution is found
    # util.raiseNotDefined()



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Initialize the priority queue with the start state and a cost of 0
    priority_queue = util.PriorityQueue()
    priority_queue.push((problem.getStartState(), [], 0), 0)
    
    # Create a set to track visited states
    visited = set()
    
    while not priority_queue.isEmpty():
        state, actions, cost = priority_queue.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            for next_state, action, step_cost in successors:
                if next_state not in visited:
                    new_actions = actions + [action]
                    new_cost = cost + step_cost
                    priority_queue.push((next_state, new_actions, new_cost), new_cost)

    return []  # Return an empty list if no solution is found

    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Initialize the priority queue with the start state, empty actions, cost, and heuristic estimate
    priority_queue = util.PriorityQueue()
    start_state = problem.getStartState()
    start_heuristic = heuristic(start_state, problem)
    priority_queue.push((start_state, [], 0, start_heuristic), 0 + start_heuristic)
    
    # Create a set to track visited states
    visited = set()
    
    while not priority_queue.isEmpty():
        state, actions, cost, h_estimate = priority_queue.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            for next_state, action, step_cost in successors:
                if next_state not in visited:
                    new_actions = actions + [action]
                    new_cost = cost + step_cost
                    new_heuristic = heuristic(next_state, problem)
                    priority_queue.push((next_state, new_actions, new_cost, new_heuristic), new_cost + new_heuristic)

    return []  # Return an empty list if no solution is found

    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
