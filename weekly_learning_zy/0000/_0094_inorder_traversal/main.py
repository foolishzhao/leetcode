from typing import Optional, List

from python3.common.define import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val]+self.inorderTraversal(root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # in-order
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

        return traversal