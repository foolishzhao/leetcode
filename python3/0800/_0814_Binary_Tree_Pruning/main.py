from python3.common.define import TreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def prune(root):
            if not root:
                return None, False

            lRes, lIncl = prune(root.left)
            rRes, rIncl = prune(root.right)

            if not lIncl and not rIncl and root.val == 0:
                return None, False

            root.left = root.right = None
            if lIncl:
                root.left = lRes
            if rIncl:
                root.right = rRes

            return root, True

        res, _ = prune(root)
        return res

    def pruneTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val:
            return None
        return root
