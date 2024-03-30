# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, sum=0) -> bool:
        # DFS
        if root is None:
            return False
        
        sum += root.val
        
        left_sum = self.hasPathSum(root.left, targetSum, sum)
        right_sum = self.hasPathSum(root.right, targetSum, sum)
        
        return left_sum or right_sum or (root.left is None and root.right is None and sum == targetSum)
        
        
        