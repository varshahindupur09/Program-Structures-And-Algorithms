############################################################
# Exam.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################

#%%
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, x):
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        dequeue_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return dequeue_data

############################################################
#  NOTHING CAN BE CHANGED BELOW
###########################################################
class Solution:
    def isEscapePossible(self, b: list[list], s: list, t: list) -> bool:
        show = False
        R = 1000000
        C = 1000000
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        work = [0]
        ans = [] #all directions you explored
        is_escape_possible = [False] #True/False
        s = Exam(R,C,b,s,t,dir,is_escape_possible,ans,work,show)
        return is_escape_possible[0]


########################################
#Nothing can be changed in class Exam
########################################
class Exam:
    def __init__(self, 
          r:'int', #Max rows
          c:'int', #Max columns
          blocked: list[list], #[[0,1],[1,0]]
          source: list, #[0,0]
          target: list, #[0,2]
          dir: list[list], #[[0,1],[1,0]] #Direction you can move from current position
          is_escape_possible: list, #True/False
          ans: list[list], #You fill all directions that you explored
          work:list, #You fill number of steps
          show: bool, #if show is True, show each step of the algorithm
        ) -> None:

        self._r = r
        self._c = c
        self._blocked = blocked
        self._dir = dir
        self._is_escape_possible = is_escape_possible
        self._ans = ans
        self._work = work
        self._show = show

        #YOU CAN HAVE your data structure. All must be private
        
        
        
        # MUST WRITE THIS ROUTINE
        self._alg() #this will fill self._is_escape_possible[0] True or False
        

    ############################################################
    # TIME: 
    # SPACE:
    ############################################################
    def _alg(self)->'None':
        print("Remove this line and write code. This code must fill self._is_escape_possible[0] = True/False")
        # Initialize BFS using SList
        queue = SList()
        queue.enqueue(self._source)
        visited = set([self._source])

        while not queue.is_empty():
            current = queue.dequeue()
            self._increment_work()  # Increment work counter
            self._append_ans(list(current))  # Append current position to ans
            
            if current == self._target:
                self._is_escape_possible[0] = True
                return

            for d in self._dir:
                next_cell = (current[0] + d[0], current[1] + d[1])
                if (0 <= next_cell[0] < self._r and 0 <= next_cell[1] < self._c and
                        next_cell not in self._blocked and next_cell not in visited):
                    queue.enqueue(next_cell)
                    visited.add(next_cell)

        self._is_escape_possible[0] = False
       

    ############################################################
    # TIME: THETA(1)
    # SPACE: THETA(1)
    ############################################################
    def _increment_work(self)->'None':
        self._work[0] += 1

    ############################################################
    # TIME: THETA(1)
    # SPACE: THETA(1)
    ############################################################
    def _append_ans(self,n:list[list]):
        self._ans.append(n)

          
############################################################
#  NOTHING CAN BE CHANGED BELOW. THIS MUST BE LAST
#
'''
    2
    4
    1 1 1 1
    1 1 1 1
    1 1 1 1
    1 1 1 1
    3
    1 0 0
    0 0 0
    0 0 1

    output
    POSSIBLE
    NOT POSSIBLE
'''
###########################################################
if (True): 
  n = int(input().strip()) #Number of testcase
  for i in range(n):
    b = [] #
    s = [0,0]        
    d = [[0,1],[1,0]] #Direction you can move from current position 
    N =  int(input().strip()) # size of matrix
    t = [N-1,N-1]
    for j in range(N):
      row = list(map(int, input().strip().split()))
      for k in range(N):
        if (row[k] == 0):
          #0 is blocked position
          b.append([j,k])
    work = [0]
    ans = [] #all directions you explored
    is_escape_possible = [False] #True/False
    s = Exam(N,N,b,s,t,d,is_escape_possible,ans,work,False)
    if (is_escape_possible[0]):
        print("POSSIBLE")
    else:
        print("NOT POSSIBLE")
# %%
