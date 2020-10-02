from python3.common.define import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(cur):
            if not cur:
                return False

            if k - cur.val in dt:
                return True

            dt[cur.val] = True
            return dfs(cur.left) or dfs(cur.right)

        dt = dict()
        return dfs(root)
