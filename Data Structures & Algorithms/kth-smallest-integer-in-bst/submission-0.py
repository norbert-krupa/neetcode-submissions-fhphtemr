# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node):
        if not node:
            return []
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)


        return  left + [node.val] + right
 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        return self.dfs(root)[k-1]
        