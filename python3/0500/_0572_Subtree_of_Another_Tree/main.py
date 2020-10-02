from python3.common.define import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or self.isSameTree(s, t)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    def isSubtree2(self, s: TreeNode, t: TreeNode) -> bool:
        def helper(root):
            if not root:
                return not t
            return root.hash == t.hash or helper(root.left) or helper(root.right)

        if not t:
            return not s
        self.treeHash(s)
        self.treeHash(t)
        return helper(s)

    def treeHash(self, root):
        if not root:
            return list()

        h = list()
        h.extend(self.treeHash(root.left))
        h.append(root.val)
        h.extend(self.treeHash(root.right))
        root.hash = h
        return h
