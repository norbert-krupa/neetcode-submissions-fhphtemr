# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node, maxSoFar):
        if not node:
            return 0


        if node.val >= maxSoFar:
            self.count += 1

        maxSoFar = max(maxSoFar, node.val)

        left = self.dfs(node.left, maxSoFar)
        right = self.dfs(node.right, maxSoFar)

        return left + right + 1


    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0
        self.dfs(root, root.val)
        
        return self.count

        