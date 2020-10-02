from python3.common.define import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(cur):
            if cur:
                if root.val < cur.val < self.res:
                    self.res = cur.val
                elif cur.val == root.val:  # only if cur val == root val, its child might eligible
                    dfs(cur.left)
                    dfs(cur.right)

        self.res = float('inf')
        dfs(root)
        return -1 if self.res == float('inf') else self.res

    def findSecondMinimumValue2(self, root: TreeNode) -> int:
        if not root or not root.left:
            return -1

        lv, rv = root.left.val, root.right.val
        if lv == root.val:
            lv = self.findSecondMinimumValue(root.left)
        if rv == root.val:
            rv = self.findSecondMinimumValue(root.right)

        if lv != -1 and rv != -1:
            return min(lv, rv)
        elif lv != -1:
            return lv
        else:
            return rv
