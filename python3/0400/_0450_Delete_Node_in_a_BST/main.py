from python3.common.define import TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key == root.val:
            if root.right:
                p = root
                cur = root.right
                while cur.left:
                    p = cur
                    cur = cur.left
                root.val = cur.val
                self.helper(p, cur)
            elif root.left:
                p = root
                cur = root.left
                while cur.right:
                    p = cur
                    cur = cur.right
                root.val = cur.val
                self.helper(p, cur)
            else:
                return None

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root

    def helper(self, p, c):
        nc = c.left if c.left else c.right
        if p.left == c:
            p.left = nc
        else:
            p.right = nc


class Solution2:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key == root.val:
            if not root.right:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
