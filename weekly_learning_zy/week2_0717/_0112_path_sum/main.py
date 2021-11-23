# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python3.common.define import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        self.dfs(root, targetSum, res)
        return any(res)
    def dfs(self,root,target,res):
        if root:
            if not root.left and not root.right and root.val == target:
                res.append(True)
            if root.left:
                self.dfs(root.left,target-root.val,res)
            if  root.right:
                self.dfs(root.right,target - root.val,res)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        st = []
        st.append((root, targetSum - root.val))
        while st:
            cur, v = st.pop()
            if not cur.left and not cur.right and v == 0:
                return True
            if cur.left:
                st.append((cur.left, v - cur.left.val))
            if cur.right:
                st.append((cur.right, v - cur.right.val))
        return False
