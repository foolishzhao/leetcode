# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional
from python3.common.define import TreeNode
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))


    # BFS
    def maxDepth2(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        depth = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            depth += 1
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

    # BFS
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    st = [root]
    ans = 0
    while st:
        nextlevel = []
        while st:
            cur = st.pop()
            if cur.left:
                nextlevel.append(cur.left)
            if cur.right:
                nextlevel.append(cur.right)
        st = nextlevel
        ans += 1
    return ans


