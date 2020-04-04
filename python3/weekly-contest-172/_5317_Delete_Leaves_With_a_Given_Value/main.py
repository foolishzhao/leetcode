from python3.common.define import TreeNode


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        while True:
            self.found = False
            root = self.helper(root, target)
            if not self.found:
                break

        return root

    def helper(self, root, target):
        if not root:
            return None

        if not root.left and not root.right:
            if root.val == target:
                self.found = True
                return None
            else:
                return root

        root.left = self.helper(root.left, target)
        root.right = self.helper(root.right, target)
        return root
