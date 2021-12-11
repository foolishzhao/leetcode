# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python3.common.define import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        while root:
            st.append(root)
            root = root.left
        while st:
            cur = st.pop()
            if k == 1:
                return cur.val
            k -= 1
            cur = cur.right
            while cur:
                st.append(cur)
                cur = cur.left
