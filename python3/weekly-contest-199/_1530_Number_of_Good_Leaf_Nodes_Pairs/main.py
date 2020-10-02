from python3.common.define import TreeNode


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(cur):
            arr = [0] * 10
            if not cur:
                return arr
            elif not cur.left and not cur.right:
                arr[0] = 1
                return arr
            else:
                lr = dfs(cur.left)
                rr = dfs(cur.right)
                for i in range(10):
                    for j in range(10):
                        if i + j + 2 <= distance:
                            nonlocal res
                            res += lr[i] * rr[j]

                for i in range(9):
                    arr[i + 1] += lr[i] + rr[i]
                return arr

        res = 0
        dfs(root)
        return res
