from typing import List


class Solution:
    # Time Limit Exceeded
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        # sort first, so when processing i-th envelope, all the satisfied x-axis envelopes are already in left.
        envelopes.sort(key=lambda x: x[0])
        n = len(envelopes)

        # dp[i] denotes max envelopes ended with i-th envelopes.
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    # Sorting the width reduces the problem by one dimension. If width is strictly increasing,
    # the problem is equivalent to finding LIS in only the height dimension. However, when there is a tie in width,
    # a strictly increasing sequence in height may not be a correct solution. For example, [[3,3] cannot fit in [3,4]].
    # Sorting height in descending order when there is a tie prevents such a sequence to be included in the solution.

    # Sorting height in descending order guarantee for each width, at most one height can be included in solution.
    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        return self.findLIS([x[1] for x in envelopes])

    def findLIS(self, nums):
        tail = []
        for num in nums:
            if not tail or num > tail[-1]:
                tail.append(num)
            else:
                tail[self.searchGreatEq(tail, num)] = num

        return len(tail)

    def searchGreatEq(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] >= target:
                if mid == left or nums[mid - 1] < target:
                    return mid
                right = mid - 1
            else:
                left = mid + 1

    # https://www.geeksforgeeks.org/box-stacking-problem-dp-22/
    # box-stacking-problem
    # solution must be increasing in area, so sort by area first, then get LIS using DP
