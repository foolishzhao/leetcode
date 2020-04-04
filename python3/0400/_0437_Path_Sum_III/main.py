from python3.common.define import TreeNode
import collections


class Solution:
    def __init__(self):
        self.res = 0

    # time complexity: O(n*log(n)), space complexity: O(log(n))
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.dfs(root, sum, list())
        return self.res

    def dfs(self, root, sum, vals):
        if not root:
            return

        vals.append(root.val)
        curSum = 0
        for v in vals[::-1]:
            curSum += v
            if curSum == sum:
                self.res += 1

        self.dfs(root.left, sum, vals)
        self.dfs(root.right, sum, vals)
        vals.pop()


class Solution2:
    # time complexity: O(n), space complexity: O(log(n))
    def pathSum(self, root: TreeNode, sum: int) -> int:
        prefixMp = collections.defaultdict(int)
        prefixMp[0] = 1

        return self.dfs(root, 0, sum, prefixMp)

    def dfs(self, root, curSum, sum, prefixMp):
        if not root:
            return 0

        curSum += root.val
        # calc before updating prefixMp, in case sum equal zero
        res = prefixMp[curSum - sum]

        prefixMp[curSum] += 1
        res += self.dfs(root.left, curSum, sum, prefixMp)
        res += self.dfs(root.right, curSum, sum, prefixMp)
        prefixMp[curSum] -= 1

        return res
