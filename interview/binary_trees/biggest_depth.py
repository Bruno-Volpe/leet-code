# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS
    def maxDepth(self, root: Optional[TreeNode], c=0) -> int:
        if root is None:
            return c
        
        c += 1
        
        max_left = self.maxDepth(root.left, c)
        max_right = self.maxDepth(root.right, c)
        
        return max_left if max_left > max_right else max_right