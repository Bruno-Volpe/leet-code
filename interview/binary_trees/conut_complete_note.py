# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#O(n) solution, O(h) space
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # DFS
        def dfs(root: Optional[TreeNode], arr=[]):
            if not root:
                return []
            
            arr.append(root.val)
            
            dfs(root.left, arr)
            dfs(root.right, arr)
            
            return (arr)
        
        elements = (dfs(root))
        return len(elements)