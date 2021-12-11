class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
        if not root:
            return []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(node.children[::-1])
        return res