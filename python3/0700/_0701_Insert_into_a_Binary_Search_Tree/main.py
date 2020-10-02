from python3.common.define import TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

    def insertIntoBST2(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left
        return root
