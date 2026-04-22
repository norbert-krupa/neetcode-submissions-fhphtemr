# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValid(self, node, lowerBound=float('-inf'), upperBound=float('inf')):
        if not node:
            return True

        if not lowerBound < node.val < upperBound:
            return False

        
        left = self.isValid(node.left, lowerBound, node.val)
        right = self.isValid(node.right, node.val, upperBound)


        return left and right



    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.isValid(root)
