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

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st = [root]
        height = 0
        end = True
        while st and end:
            nextlevel = []
            for i in range(len(st)):
                cur = st.pop()
                if cur.left:
                    nextlevel.append(cur.left)
                if cur.right:
                    nextlevel.append(cur.right)
                if not cur.left and not cur.right:
                    height += 1
                    end = False
                    break
            if end:
                height += 1
                st = nextlevel
        return height