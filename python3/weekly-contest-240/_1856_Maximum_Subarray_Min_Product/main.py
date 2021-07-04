from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        lb, rb = [0] * n, [n - 1] * n

        st = list()
        for i in range(n):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                lb[i] = st[-1] + 1
            st.append(i)

        st = list()
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                rb[i] = st[-1] - 1
            st.append(i)

        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        res = 0
        for i in range(n):
            res = max(res, nums[i] * (preSum[rb[i] + 1] - preSum[lb[i]]))
        return res % (10 ** 9 + 7)
