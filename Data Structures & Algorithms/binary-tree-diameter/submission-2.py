# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getDepth(self, node):

        if not node:
            return 0
        
        left_depth = self.getDepth(node.left)
        right_depth = self.getDepth(node.right)

        self.best_diameter = max(self.best_diameter, left_depth + right_depth)

        return max(left_depth, right_depth) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.best_diameter = 0

        self.getDepth(root)

        return self.best_diameter


