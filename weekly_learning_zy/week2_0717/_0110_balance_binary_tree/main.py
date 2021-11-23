# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python3.common.define import TreeNode


class Solution:

    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(
                root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

