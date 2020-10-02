from python3.common.define import TreeNode


class Solution:
    # recursive
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return None

        if d == 1:
            res = TreeNode(v)
            res.left = root
            return res

        if d == 2:
            nl, nr = TreeNode(v), TreeNode(v)
            nl.left = root.left
            root.left = nl

            nr.right = root.right
            root.right = nr
        else:
            root.left = self.addOneRow(root.left, v, d - 1)
            root.right = self.addOneRow(root.right, v, d - 1)
        return root

    # iterative
    def addOneRow2(self, root: TreeNode, v: int, d: int) -> TreeNode:
        dummy = TreeNode(0)
        dummy.left = root

        q = [dummy]
        for _ in range(d - 1):
            q = [y for x in q for y in (x.left, x.right) if y]

        for node in q:
            nl, nr = TreeNode(v), TreeNode(v)
            nl.left = node.left
            node.left = nl
            nr.right = node.right
            node.right = nr

        return dummy.left
