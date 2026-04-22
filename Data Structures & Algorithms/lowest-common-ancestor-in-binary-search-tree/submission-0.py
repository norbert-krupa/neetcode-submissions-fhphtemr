# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node):
        if not node:
            return [None]
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        traversal = [node.val] + left + right
        self.traversals[node] = traversal

        return traversal

        

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        self.traversals = {}
        self.dfs(root)



        

        for node, traversal in self.traversals.items():
            if p.val in traversal and q.val in traversal:
                return node
        
        
        