from python3.common.define import TreeNode


class Solution:
    def __init__(self):
        self.greatSum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        self.convertBST(root.right)
        root.val += self.greatSum
        self.greatSum = root.val
        self.convertBST(root.left)
        return root
