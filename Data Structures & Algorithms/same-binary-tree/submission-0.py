# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def bfs(self, root):
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if not node:
                result.append(None)
            else:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        return result
        


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        return self.bfs(p) == self.bfs(q)

