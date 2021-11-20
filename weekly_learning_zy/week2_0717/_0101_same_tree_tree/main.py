# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from python3.common.define import TreeNode

class Solution:
    def isMirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
        return p is q

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        if p and q:
            return p.val == q.val and self.isMirror(p, q)
        return p is q