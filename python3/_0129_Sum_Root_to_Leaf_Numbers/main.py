from python3.common.define import TreeNode
from typing import List


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        nums = []
        self.sumNumbersHelper(nums, root, 0)
        return sum(nums)

    def sumNumbersHelper(self, nums: List[int], root: TreeNode, cur: int):
        cur = cur * 10 + root.val
        if not root.left and not root.right:
            nums.append(cur)
        elif not root.left:
            self.sumNumbersHelper(nums, root.right, cur)
        elif not root.right:
            self.sumNumbersHelper(nums, root.left, cur)
        else:
            self.sumNumbersHelper(nums, root.left, cur)
            self.sumNumbersHelper(nums, root.right, cur)
