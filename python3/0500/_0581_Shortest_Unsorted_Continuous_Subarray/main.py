from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)

        i, j, n = 0, len(nums) - 1, len(nums)
        while i < n and nums[i] == sortedNums[i]:
            i += 1

        while j > i and nums[j] == sortedNums[j]:
            j -= 1

        return j - i + 1

    # end = most right element having greater elements on the left side.
    # begin = most left element having smaller elements on the right side.
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        n = len(nums)

        end, mx = 0, nums[0]
        for i in range(1, n):
            mx = max(mx, nums[i])
            if nums[i] < mx:
                end = i

        begin, mn = 1, nums[-1]
        for i in range(n - 2, -1, -1):
            mn = min(mn, nums[i])
            if nums[i] > mn:
                begin = i

        return end - begin + 1
