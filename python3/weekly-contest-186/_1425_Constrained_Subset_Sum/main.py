from typing import List
import collections


class Solution:
    # dp[i] is the maximum sum we can get from nums[:i] and nums[i] is guaranteed to be included.
    # dp[0] = nums[0]
    # dp[i] = max(dp[i - k], dp[i-k+1], ..., dp[i - 1], 0) + x
    # use a deque to save max dp value from previous k dp
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        deque = collections.deque()
        n = len(nums)
        for i in range(n):
            nums[i] += deque[0][1] if deque else 0
            while deque and deque[-1][1] <= nums[i]:
                deque.pop()
            if nums[i] > 0:
                deque.append((i, nums[i]))
            if i >= k and deque and deque[0][0] == i - k:
                deque.popleft()

        return max(nums)
