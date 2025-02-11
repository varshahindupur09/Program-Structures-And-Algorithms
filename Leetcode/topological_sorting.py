#  Topological Sorting (similar to Kahn’s Algorithm for finding the longest path in a Directed Acyclic Graph). The idea is to remove leaves level by level until we reach the root(s) of the Minimum Height Tree (MHT).
# from collections import defaultdict
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1:0,2,3    0:1  2:1 3:1
        if n == 1:
            return [0]

        graph = {i: set() for i in range(n)}
        # adj = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)

        leaves = deque([ node for node in graph if len(graph[node]) == 1 ])
        print("leaves ", leaves)

        remaining_nodes = n

        while remaining_nodes> 2:        
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves
            print("remaining_nodes ", remaining_nodes, num_leaves)
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                print("leaf ", leaf)
                neighbor = graph[leaf].pop()
                print("neighbor ", neighbor)
                graph[neighbor].remove(leaf)
                print("graph ", graph)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
                print("leaves ", leaves)
                
        return list(leaves)

############################################################
EXECUTION:
############################################################
Test case: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
O/P:
leaves  deque([0, 1, 2, 5])
remaining_nodes  2 4
leaf  0
neighbor  3
graph  {0: set(), 1: {3}, 2: {3}, 3: {1, 2, 4}, 4: {3, 5}, 5: {4}}
leaves  deque([1, 2, 5])
leaf  1
neighbor  3
graph  {0: set(), 1: set(), 2: {3}, 3: {2, 4}, 4: {3, 5}, 5: {4}}
leaves  deque([2, 5])
leaf  2
neighbor  3
graph  {0: set(), 1: set(), 2: set(), 3: {4}, 4: {3, 5}, 5: {4}}
leaves  deque([5, 3])
leaf  5
neighbor  4
graph  {0: set(), 1: set(), 2: set(), 3: {4}, 4: {3}, 5: set()}
leaves  deque([3, 4])
