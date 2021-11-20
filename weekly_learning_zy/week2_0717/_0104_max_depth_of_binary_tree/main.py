# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from python3.common.define import TreeNode
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        depth = 1
        if root and root.left and root.right:
            depth += max(self.maxDepth(root.left), self.maxDepth(root.right))
        elif not root.left:
            depth += self.maxDepth(root.right)
        else:
            depth += self.maxDepth(root.left)
        return depth

    # BFS
    def maxDepth2(self, root: Optional[TreeNode]) -> int:

        if not root:ds
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