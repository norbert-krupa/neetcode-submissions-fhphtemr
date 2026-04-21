# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node, addToDict=False):
        if not node:
            return [None]
        
        if addToDict:
            left = self.dfs(node.left, True)
            right = self.dfs(node.right, True)
        else:
            left = self.dfs(node.left)
            right = self.dfs(node.right)

        traversal = [node.val] + left + right

        if addToDict:
            self.traversals[node] = traversal

        return traversal

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.traversals = {}

        self.dfs(root, True)

        sub_traversal = self.dfs(subRoot)

        for _, traversal in self.traversals.items():
            if traversal == sub_traversal:
                return True

        return False








        