# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python3.common.define import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
        elif not root.left:
            return self.minDepth(root.right) + 1
        else:
            return self.minDepth(root.left) + 1