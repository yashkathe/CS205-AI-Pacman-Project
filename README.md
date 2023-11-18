# Pacman project

Soure: http://ai.berkeley.edu/search.html

## Check Test Cases

- ### Test Case 1

```bash
python autograder.py --q q1
```

- ### Test Case 2

```bash
python autograder.py --q q2
```

- ### Test Case 3

```bash
python autograder.py --q q3
```

- ### Test Case 4

```bash
python autograder.py --q q4
```

- ### Test Case 5

```bash
python autograder.py --q q5
```

- ### Test Case 6

```bash
python autograder.py --q q6
```

## Report

### Question 1: Finding a Fixed Food Dot using Depth First Search

Depth First Search (DFS) is a way to explore a graph or tree structure by going
as deep as possible along one branch before backtracking

Our program starts by creating a stack and a set to track visited states. We
then push the initial state and an empty list of actions onto the stack. It then
enters a while loop which runs as long as the stack is not empty. Inside the
loop, it pops the top state and its associated actions from the stack and checks
if the current state is the goal state. If the goal state is reached, the
function returns the list of actions as the solution.

If the current state is not the goal state and has not been visited before, the
algorithm marks it as visited and explores its successor states. For each
unvisited successor state, it updates the list of actions and pushes the
successor state to the stack which has to be explored further . The algorithm
repeats this process until a solution is found or all possibilities are
exhausted. If no solution is found, the function returns an empty list to
indicate that there is no path to the goal state.

The Pacman board will show an overlay of the states explored, and the order in
which they were explored (brighter red means earlier exploration). Is the
exploration order what you would have expected? Does Pacman actually go to all
the explored squares on his way to the goal?

We can observe that DFS follows the first path as deeply as possible along a
branch of the tree before advancing to the next branch. This is the expected
exploration order for DFS. However, DFS does not always guarantee the best
possible optimal solution, and the exploration order may not align with
expectations in this regard. Pac-Man might bypass certain states while exploring
others more extensively in its quest to find the goal state.

### Question 2: Breadth First Search

Breadth-First Search (BFS) is an algorithm for exploring or traversing a graph
or tree by visiting all neighbors of a node before moving to the next level of
neighbors

We start by creating a queue and a set to track visited states. Now push the
initial state and empty list of actions in the queue. We now enter the while
loop which will run till the queue is not empty. Inside the loop we dequeue the
state and its associated actions. If the state we dequeue is the goal state then
we return its list of actions as the solution. If it’s not the goal state we
mark it as visited and get the successors of the current state along with its
associated actions and step costs. And for each unvisited successor we update
the list of actions and enqueue it for visiting further. If no solution is found
we return an empty list.

### Question 3 : Varying the Cost Function

Uniform Cost Search (UCS) is a graph search algorithm that finds the path with
the lowest cost in a weighted graph, where each edge has a cost associated with
it.

Our program begins by setting up a priority queue to monitor the states that
require exploration, each initially assigned a cost of 0. We also maintain a
record of visited states. The main loop continues as long as the priority queue
isn't empty. During each iteration, we check if the current state has reached
the goal. If it hasn't been visited yet, we add it to the list of visited
states. Furthermore, we examine the current state's successors, which are the
states that can be reached from the current one. These successors come with
associated actions and the costs involved in transitioning from the current
state to these successors. The goal is identified with the most cost-effective
path.

### Question 4: A\* Search

A\* search is a heuristic searching algorithm which allows to find the most
effective path from the initial node to the destination node with the least
possible cost.

We start off by initializing the state, action, cost and heuristic estimate and
keep a track of the node that we already visited so that we don't revisit the
same node again. We iterate along the loop starting with the state with lowest
combined cost and heuristic estimate. Once we reach the goal state, return to
the actions as a solution. If not, we explore the successor and update the
actions, cost and estimate.We update the queue with the successor information
until we find the solution. If a solution is not found then we return an empty
list.

### 1. What happens on openMaze for the various search strategies?

#### Depth-First Search (DFS)

DFS is a non-optimal uninformed search algorithm that thoroughly explores one
path before backtracking. On openMaze, DFS might become trapped in the
exploration of a single long path and, as a result, could miss finding the
shortest path to the goal. This is because DFS doesn't take into account the
overall cost or heuristic information to guide its exploration, which makes it
less effective in mazes with intricate layouts.

#### Breadth-First Search (BFS)

BFS is an optimal uninformed search algorithm that explores all paths at a given
depth level before moving to deeper levels. On openMaze, BFS will systematically
explore all available paths at each level, ensuring that it eventually finds the
shortest path to the goal. However, BFS can be less efficient than other
algorithms, especially in large mazes, as it expands all possible paths
regardless of their cost or estimated distance to the goal.

#### Uniform Cost Search (UCS)

UCS is an excellent informed search algorithm that picks the cheapest paths
first, leading to the most cost-effective solutions on openMaze. It's more
efficient than BFS because it avoids expensive routes. However, when multiple
paths have the same cost, UCS may not always pick the absolute shortest one.

#### A Search\*

A* Search is an optimal informed search algorithm that combines actual cost with
an estimated cost to the goal. On openMaze, A* will consider both cost and
heuristic information to guide exploration, making it more efficient than both
DFS and BFS. A* typically finds optimal solutions, but the heuristic value can
influence its performance. If the heuristic is inaccurate, A* may explore paths
that are not optimal.

#### Performance Comparison

In general, A\* is the most efficient and effective search algorithm for
openMaze, as it combines the advantages of informed and uninformed search. UCS
can also be efficient in finding the shortest path, but it may not always
consider heuristic information. BFS is guaranteed to find the shortest path, but
it can be less efficient than other algorithms. DFS is the least efficient and
effective algorithm, as it is prone to getting stuck in long, winding paths.

### Question 5: Finding All the Corners

For finding all the corners of the map using Breadth-First Search (BFS)
approach, we have written an algorithm that keeps track of the visited corners.
Every step of the procedure involves assessing the current position to see if it
is a corner or not. If it is detected as a corner, all the visited nodes are
marked as visited. We further proceed to generate a set of successor states by
exploring movement in all directions i.e (north, south, east, and west). For
each of these successor states, we check if it hits the wall or not.If it is not
hitting the wall, then we add the successor state to the list of successors.This
iterative process gradually discovers a route that effectively traverses the map
while guaranteeing that every corner is explored and visited.

### Question 6: Corners Problem: Heuristic

To find the corners of the map using a nontrivial A\* search, we created a
heuristic function that estimates the cost to reach the goal state from the
current state. A good heuristic function will provide an accurate estimate of
the cost, which can help the search algorithm to find the goal state more
quickly. We then created a cornersHeuristic function which estimates the cost to
reach the closest unvisited corner. The function first checks if the current
state is a goal state. If it is, the function returns 0. Otherwise, the function
obtains the current position and list of visited corners.

The function then iterates over all of the corners and omits the visited
corners. For each unvisited corner, the function computes the Manhattan distance
to the corner. The Manhattan distance is a simple way to estimate the cost of
moving from one point to another. Further, the function updates the maximum
Manhattan distance if it is greater than the current maximum. Finally, the
function returns the maximum Manhattan distance.
