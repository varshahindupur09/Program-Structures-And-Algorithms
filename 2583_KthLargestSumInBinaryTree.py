################################################################################
QUESTION
################################################################################
You are given the root of a binary tree and a positive integer k.
The level sum in the tree is the sum of the values of the nodes that are on the same level.
Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
Note that two nodes are on the same level if they have the same distance from the root.
Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n

################################################################################
SOLUTION 1: BFS
################################################################################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        res = []
        # print(q)

        while q:
            n = len(q)
            # print(n) # output limit exceeded
            level_sum = 0

            for _ in range(n):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level_sum)

        if k > len(res):
            return -1

        res.sort(reverse=True)

        return res[k-1]

################################################################################
SOLUTION 2: DFS
################################################################################

import heapq
from typing import Optional

class TreeNode:
    def __init__(self, left: None, right: None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        max_heap = []

        def dfs(childArray):
            if not childArray:
                return 
            sum_val = 0
            nextChildArray = []
            for child in childArray:
                sum_val += child.val

                if child.left:
                    nextChildArray.append(child.left)
                if child.right:
                    nextChildArray.append(child.right)
                
            heapq.heappush(max_heap, -sum_val) # Using a min-heap with negative values to simulate max-heap
            dfs(nextChildArray)

        dfs([root])

        if len(max_heap) < k:
            return -1

        top = -1
        while k:
            top = -heapq.heappop(max_heap)
            k -= 1

        return top if top != -1 else -1
        
