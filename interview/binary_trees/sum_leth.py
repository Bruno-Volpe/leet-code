from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode], sum=0) -> int:
        if root is None:
            return 0

        sum = sum * 10 + root.val

        if root.left is None and root.right is None:
            return sum

        return self.sumNumbers(root.left, sum) + self.sumNumbers(root.right, sum)
        