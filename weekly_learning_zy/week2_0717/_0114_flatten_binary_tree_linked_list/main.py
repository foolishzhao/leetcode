# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python3.common.define import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        leftres = root.left
        rightres = root.right
        root.left = None
 rl
        if leftres:
            root.right = leftres
            while leftres.right:
                leftres = leftres.right
            leftres.right = rightres
        else:
            root.right = rightres


