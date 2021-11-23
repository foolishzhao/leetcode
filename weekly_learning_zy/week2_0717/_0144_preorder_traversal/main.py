from typing import Optional, List

from python3.common.define import TreeNode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)