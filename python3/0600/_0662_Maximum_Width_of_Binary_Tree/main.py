from python3.common.define import TreeNode


class Solution:
    # bfs
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        q, res = [(root, 0)], 0
        while q:
            sz = len(q)
            res = max(res, q[sz - 1][1] - q[0][1] + 1)
            for _ in range(sz):
                cur, i = q.pop(0)
                if cur.left:
                    q.append((cur.left, 2 * i + 1))
                if cur.right:
                    q.append((cur.right, 2 * i + 2))
        return res

    # dfs
    def widthOfBinaryTree2(self, root: TreeNode) -> int:
        def dfs(cur, depth, i):
            if not cur:
                return 0

            if depth == len(leftMost) + 1:
                leftMost.append(i)

            res = i - leftMost[depth - 1] + 1
            res = max(res, dfs(cur.left, depth + 1, 2 * i + 1))
            res = max(res, dfs(cur.right, depth + 1, 2 * i + 2))
            return res

        leftMost = list()
        return dfs(root, 1, 0)
