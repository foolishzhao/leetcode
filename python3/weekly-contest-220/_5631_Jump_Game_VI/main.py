from typing import List


class Solution:
    # incorrect, as dp[0] is not really exist, it may affect following calculation
    def maxResult(self, nums: List[int], k: int) -> int:
        n, st = len(nums), [0]
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = nums[i] + dp[st[0]]
            while st and dp[st[-1]] < dp[i + 1]:
                st.pop()
            st.append(i + 1)

            if i + 1 - st[0] == k + 1:
                st.pop(0)
        return dp[n]

    def maxResult2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp, st = [0] * n, [0]
        dp[0] = nums[0]
        for i in range(1, n):
            if i - st[0] == k + 1:
                st.pop(0)

            dp[i] = dp[st[0]] + nums[i]
            while st and dp[st[-1]] <= dp[i]:
                st.pop()
            st.append(i)

        return dp[-1]
