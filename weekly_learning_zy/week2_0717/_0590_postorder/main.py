"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [(root,False)]
        while stack:
            node ,visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node,True))
                    for x in node.children[::-1]:
                        stack.append((x,False))
        return res

    class Solution:
        def recursion(self, root, res):
            for child in root.children:
                self.recursion(child, res)
            res.append(root.val)

        def postorder(self, root: 'Node') -> List[int]:
            if not root:
                return []
            res = []
            self.recursion(root, res)
            return res

    class Solution:
        def postorder(self, root: 'Node') -> List[int]:
            if not root:
                return []
            res = []
            for x in root.children:
                res = res + self.postorder(x)
            res += [root.val]
            return res