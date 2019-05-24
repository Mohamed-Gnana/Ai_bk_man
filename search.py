# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
from math import *
class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           
class Node:
    def __init__(self, route, cost):
        self.route = route
        self.cost = cost
def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  print("Start:", problem.getStartState())
  print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
  print("Start's successors:", problem.getSuccessors(problem.getStartState()))

  explored = []
  fringe = util.Stack() #define the fringe as a Stack. You can check util.py
  fringe.push([(problem.getStartState(), "Stop", 0)]) # adding the first node into the fringe
  #please note that each node is represented using the path from the starting node to the it
  while not fringe.isEmpty():
      # print ("fringe: ", fringe.heap)
      path = fringe.pop() # pop a node from the fringe
      # print "path len: ", len(path)
      # print "path: ", path

      s = path[len(path) - 1]
      s = s[0]
      # print "s: ", s
      if problem.isGoalState(s):
          # print "FOUND SOLUTION: ", [x[1] for x in path]
          return [x[1] for x in path][1:]

      if s not in explored:
          explored.append(s) # append the state to explored
          # print "EXPLORING: ", s

          for successor in problem.getSuccessors(s):
              # print "SUCCESSOR: ", successor
              if successor[0] not in explored:
                  successorPath = path[:]
                  successorPath.append(successor)
                  # print "successorPath: ", successorPath
                  fringe.push(successorPath) # push the sucessorPath into fringe
          # else:
          # print successor[0], " IS ALREADY EXPLORED!!"

  return []

  util.raiseNotDefined()

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  print("Start:", problem.getStartState())
  print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
  print("Start's successors:", problem.getSuccessors(problem.getStartState()))

  explored = []
  fringe = util.Queue() #define the fringe as a Stack. You can check util.py
  fringe.push([(problem.getStartState(), "Stop", 0)]) # adding the first node into the fringe
  #please note that each node is represented using the path from the starting node to the it
  while not fringe.isEmpty():
      # print ("fringe: ", fringe.heap)
      path = fringe.pop() # pop a node from the fringe
      # print "path len: ", len(path)
      # print "path: ", path
      #print(path)
      s = path[len(path) - 1]
      s = s[0]
      # print "s: ", s
      if problem.isGoalState(s):
          # print "FOUND SOLUTION: ", [x[1] for x in path]
          #print("Found Sol", [x[1] for x in path][1:])
          return [x[1] for x in path][1:]

      if s not in explored:
          explored.append(s) # append the state to explored
          # print "EXPLORING: ", s

          for successor in problem.getSuccessors(s):
              print(successor)
              # print "SUCCESSOR: ", successor
              if successor[0] not in explored:
                  successorPath = path[:]
                  successorPath.append(successor)
                  # print "successorPath: ", successorPath
                  fringe.push(successorPath) # push the sucessorPath into fringe
          # else:
          # print successor[0], " IS ALREADY EXPLORED!!"

  return []

  util.raiseNotDefined()

def heruisitic1(l):
    sublist = l[len(l) - 1]
    pos = sublist[0]
    xpos = pos[0]
    ypos = pos[1]
    dist = sublist[2]
    dist += abs(xpos - 1) + abs(ypos - 1)
    return dist
def heruisitic2(l):
    sublist = l[len(l) - 1]
    pos = sublist[0]
    xpos = pos[0]
    ypos = pos[1]
    dist = sublist[2]
    dist += sqrt(abs(xpos - 1)**2 + abs(ypos - 1)**2)
    return dist
def uniformCostSearch2(problem):

  explored = []
  fringe = util.PriorityQueueWithFunction(len) #define the fringe as a Stack. You can check util.py
  fringe.push([(problem.getStartState(), "Stop", 0)]) # adding the first node into the fringe
  #please note that each node is represented using the path from the starting node to the it
  while not fringe.isEmpty():
      # print ("fringe: ", fringe.heap)
      path = fringe.pop() # pop a node from the fringe
      # print "path len: ", len(path)
      # print "path: ", path
      #print(path)
      s = path[len(path) - 1]
      s = s[0]
      # print "s: ", s
      if problem.isGoalState(s):
          # print "FOUND SOLUTION: ", [x[1] for x in path]
          #print("Found Sol", [x[1] for x in path][1:])
          return [x[1] for x in path][1:]

      if s not in explored:
          explored.append(s) # append the state to explored
          # print "EXPLORING: ", s

          for successor in problem.getSuccessors(s):
              #print(successor)
              # print "SUCCESSOR: ", successor
              if successor[0] not in explored:
                  successorPath = path[:]
                  successorPath.append(successor)
                  # print "successorPath: ", successorPath
                  fringe.push(successorPath) # push the sucessorPath into fringe
          # else:
          # print successor[0], " IS ALREADY EXPLORED!!"

  return []

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  vis = []
  fringe = util.PriorityQueue()
  fringe.push([(problem.getStartState(), "Stop", 0)], 0)
  while not fringe.isEmpty():
      path = fringe.pop()
      state = path[len(path) - 1]
      s = state[0]
      cost = state[2]
      if problem.isGoalState(s):
          return [x[1] for x in path][1:]
      if s not in vis:
          vis.append(s)
          for successor in problem.getSuccessors(s):
              tmp_path = path[:]
              tmp_successor =(successor[0], successor[1], cost + 1)
              tmp_path.append(tmp_successor)
              fringe.push(tmp_path, tmp_successor[2])
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch1(problem, heuristic=heruisitic1):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  vis = []
  fringe = util.PriorityQueueWithFunction(heruisitic1)
  fringe.push([(problem.getStartState(), "Stop", 0)])
  while not fringe.isEmpty():
      path = fringe.pop()
      state = path[len(path) - 1]
      s = state[0]
      cost = state[2]
      print(cost)
      if problem.isGoalState(s):
          return [x[1] for x in path][1:]
      if s not in vis:
          vis.append(s)
          for successor in problem.getSuccessors(s):
              tmp_path = path[:]
              tmp_successor =(successor[0], successor[1], cost + 1)
              tmp_path.append(tmp_successor)
              fringe.push(tmp_path)
  util.raiseNotDefined()
def aStarSearch2(problem, heuristic=heruisitic2):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  vis = []
  fringe = util.PriorityQueueWithFunction(heruisitic2)
  fringe.push([(problem.getStartState(), "Stop", 0)])
  while not fringe.isEmpty():
      path = fringe.pop()
      state = path[len(path) - 1]
      s = state[0]
      cost = state[2]
      print(cost)
      if problem.isGoalState(s):
          return [x[1] for x in path][1:]
      if s not in vis:
          vis.append(s)
          for successor in problem.getSuccessors(s):
              tmp_path = path[:]
              tmp_successor =(successor[0], successor[1], cost + 1)
              tmp_path.append(tmp_successor)
              fringe.push(tmp_path)

  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch1
ucs = uniformCostSearch
ucs2 = uniformCostSearch2
astar2 = aStarSearch2
