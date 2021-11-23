class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(cur):
            if not cur.left and not cur.right:
                return cur.val, cur.val
            elif not cur.left:
                rRes, rMax = dfs(cur.right)
                return max(rRes, cur.val + max(rMax, 0)), cur.val + max(rMax, 0)
            elif not cur.right:
                lRes, lMax = dfs(cur.left)
                return max(lRes, cur.val + max(lMax, 0)), cur.val + max(lMax, 0)
            else:
                lRes, lMax = dfs(cur.left)
                rRes, rMax = dfs(cur.right)
                return max(lRes, rRes, max(lMax, 0) + max(rMax, 0) + cur.val), cur.val + max(lMax, rMax, 0)

        if not root:
            return 0

        res, _ = dfs(root)
        return res


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(cur):
            if not cur:
                return float('-inf'), float('-inf')

            lRes, lMax = dfs(cur.left)
            rRes, rMax = dfs(cur.right)
            return max(lRes, rRes, cur.val + max(lMax, 0) + max(rMax, 0)), cur.val + max(lMax, rMax, 0)

        if not root:
            return 0

        res, _ = dfs(root)
        return res