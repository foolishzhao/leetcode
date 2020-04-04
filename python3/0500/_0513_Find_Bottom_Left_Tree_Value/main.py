from python3.common.define import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res, _ = self.dfs(root, 0)
        return res

    def dfs(self, root, d):
        if not root.left and not root.right:
            return root.val, d
        elif not root.left:
            return self.dfs(root.right, d + 1)
        elif not root.right:
            return self.dfs(root.left, d + 1)
        else:
            lv, ld = self.dfs(root.left, d + 1)
            rv, rd = self.dfs(root.right, d + 1)
            return (lv, ld) if ld >= rd else (rv, rd)

    def findBottomLeftValue2(self, root: TreeNode) -> int:
        q, cur = [root], root
        while q:
            cur = q.pop(0)
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
        return cur.val
