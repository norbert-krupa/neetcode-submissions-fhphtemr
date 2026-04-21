# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    balanced = True

    def getDepth(self, node):

        if not node:
            return 0
        
        left = self.getDepth(node.left)
        right = self.getDepth(node.right)

        if abs(left - right) > 1:
            self.balanced = False

        return max(left, right) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.getDepth(root)

        return self.balanced


