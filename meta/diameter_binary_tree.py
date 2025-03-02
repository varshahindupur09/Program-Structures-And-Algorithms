# TC = O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.diameter

    def helper(self, node: TreeNode):
        if not node:
            return 0
        
        left_depth = self.helper(node.left)
        right_depth = self.helper(node.right)

        current_diamter = left_depth + right_depth

        self.diameter = max(self.diameter, current_diamter)

        return max(left_depth, right_depth) + 1



