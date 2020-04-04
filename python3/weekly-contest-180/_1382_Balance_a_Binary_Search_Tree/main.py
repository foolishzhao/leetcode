from python3.common.define import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = self.preOrder(root)
        return self.build(vals, 0, len(vals) - 1)

    def build(self, vals, b, e):
        if b > e:
            return None

        m = (e - b) // 2 + b
        root = TreeNode(vals[m])
        root.left = self.build(vals, b, m - 1)
        root.right = self.build(vals, m + 1, e)
        return root

    def preOrder(self, root):
        if not root:
            return list()

        res = self.preOrder(root.left)
        res.append(root.val)
        res.extend(self.preOrder(root.right))

        return res
