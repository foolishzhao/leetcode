from typing import List
import functools


class Solution:
    # Time Limit Exceeded
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        @functools.lru_cache(None)
        def dp(i, section):
            if i < section * k:
                return 0, list()

            if section == 1:
                curMax, curIdx = 0, 0
                for j in range(i - k + 1):
                    if sectionSum[j] > curMax:
                        curMax, curIdx = sectionSum[j], j
                return curMax, [curIdx]

            s1, index1 = dp(i - 1, section)
            s2, index2 = dp(i - k, section - 1)
            s2 += sectionSum[i - k]
            return (s1, index1) if s1 >= s2 else (s2, index2 + [i - k])

        n, sectionSum, cur = len(nums), list(), 0
        for i, num in enumerate(nums):
            cur += num
            if i >= k - 1:
                sectionSum.append(cur)
                cur -= nums[i - k + 1]
        _, res = dp(n, 3)
        return res

    # dp(i, section): for nums[:i], and section (can be 1, 2, 3), return maxSumOfSubarray and corresponding indexes
    # for maxSumOfSubarray resp, up to whether (i-1)-th num is used, it satisfies:
    #   dp(i, section) = max(dp(i - 1, section), sectionSum[i - k] + dp(i - k, section - 1))
    #
    # for list data in resp, do not change it
    def maxSumOfThreeSubarrays2(self, nums: List[int], k: int) -> List[int]:
        @functools.lru_cache(None)
        def dp(i, section):
            if i < section * k:
                return 0, list()

            # for section 1, also use dp to speed up
            s1, index1 = dp(i - 1, section)
            if section == 1:
                s2, index2 = sectionSum[i - k], [i - k]
            else:
                s2, index2 = dp(i - k, section - 1)
                s2 += sectionSum[i - k]
                index2 = index2 + [i - k]
            return (s1, index1) if s1 >= s2 else (s2, index2)

        n, sectionSum, cur = len(nums), list(), 0
        for i, num in enumerate(nums):
            cur += num
            if i >= k - 1:
                sectionSum.append(cur)
                cur -= nums[i - k + 1]
        _, res = dp(n, 3)
        return res

    def maxSumOfThreeSubarrays3(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        secSum, left, right, cur = [0] * n, [0] * n, [0] * n, 0
        for i, num in enumerate(nums):
            cur += num
            if i >= k - 1:
                secSum[i - k + 1] = cur
                cur -= nums[i - k + 1]

        for i in range(1, n - k + 1):
            left[i] = left[i - 1]
            if secSum[i] > secSum[left[i - 1]]:
                left[i] = i

        right[n - k] = n - k
        for i in range(n - k - 1, -1, -1):
            right[i] = right[i + 1]
            if secSum[i] >= secSum[right[i + 1]]:
                right[i] = i

        maxSum, res = 0, list()
        for i in range(k, n - 2 * k + 1):
            if secSum[left[i - k]] + secSum[i] + secSum[right[i + k]] > maxSum:
                maxSum = secSum[left[i - k]] + secSum[i] + secSum[right[i + k]]
                res = [left[i - k], i, right[i + k]]
        return res


if __name__ == '__main__':
    Solution().maxSumOfThreeSubarrays3([1, 2, 1, 2, 6, 7, 5, 1], 2)
