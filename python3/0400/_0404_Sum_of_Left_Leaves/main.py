from python3.common.define import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.helper(root.left, True) + self.helper(root.right, False)

    def helper(self, root, isLeft):
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val if isLeft else 0

        return self.helper(root.left, True) + self.helper(root.right, False)
