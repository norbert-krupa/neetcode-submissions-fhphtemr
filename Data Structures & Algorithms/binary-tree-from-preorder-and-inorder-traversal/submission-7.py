# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == []:
            return None

        indices = {}
        for i in range(len(inorder)):
            indices[inorder[i]] = i

        root = preorder.pop(0)
        rootIndex = indices[root]

        leftInOrder = inorder[:rootIndex]
        rightInOrder = inorder[rootIndex+1:]

        leftPreOrder = preorder[:rootIndex]
        rightPreOrder = preorder[rootIndex:]

        left = self.buildTree(leftPreOrder, leftInOrder)
        right = self.buildTree(rightPreOrder, rightInOrder)

        return TreeNode(root, left, right)

        
        