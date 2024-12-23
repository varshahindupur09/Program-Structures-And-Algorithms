# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

########################################################################
SOLUTION: DFS (TC: O(n) , SC: O(n))
########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 40+9=49 therefore 490+5=495
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, current_sum: int) -> int:
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum

            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        return dfs(root, 0)

########################################################################
SOLUTION: DFS (TC: O(n) , SC: O(n)), Stack
########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total_sum = 0
        stack = [(root, 0)]

        while stack:
            node, current_sum = stack.pop()
            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                total_sum += current_sum
            else:
                if node.right:
                    stack.append((node.right, current_sum))
                if node.left:
                    stack.append((node.left, current_sum))

        return total_sum
        
            
