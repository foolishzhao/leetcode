from python3.common.define import TreeNode
from typing import List


class Solution:
    # O(n^2) worst time complexity
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mi, mv = -1, float('-inf')
        for i, v in enumerate(nums):
            if v > mv:
                mi, mv = i, v

        root = TreeNode(mv)
        root.left = self.constructMaximumBinaryTree(nums[:mi])
        root.right = self.constructMaximumBinaryTree(nums[mi + 1:])
        return root

    # https://leetcode.com/problems/maximum-binary-tree/discuss/106156/Java-worst-case-O(N)-solution/143674
    # O(n) time complexity, O(n) space complexity
    def constructMaximumBinaryTree2(self, nums: List[int]) -> TreeNode:
        st = list()
        for num in nums:
            cur = TreeNode(num)
            while st and st[-1].val < cur.val:
                cur.left = st.pop()
            if st:
                st[-1].right = cur
            st.append(cur)

        return st[0]
