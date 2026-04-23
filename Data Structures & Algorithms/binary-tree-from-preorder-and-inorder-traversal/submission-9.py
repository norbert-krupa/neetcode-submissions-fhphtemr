# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def recursiveBuild(self, preorder, inorder, start, end):
        if start > end:
            return None

        root = preorder.pop(0)
        rootIndex = self.indices[root]

        left = self.recursiveBuild(preorder, inorder, start, rootIndex-1)
        right = self.recursiveBuild(preorder, inorder, rootIndex+1, end)

        return TreeNode(root, left, right)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.indices = {}

        for i in range(len(inorder)):
            self.indices[inorder[i]] = i

        root = self.recursiveBuild(preorder, inorder, 0, len(inorder)-1)

        return root

        
        