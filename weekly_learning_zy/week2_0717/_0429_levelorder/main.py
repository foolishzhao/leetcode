"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur_level ,size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.children:
                    queue.extend(node.children)
                cur_level.append(node.val)
            res.append(cur_level)
        return res