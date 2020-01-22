from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        cur, i, n = 0, 0, len(nums)
        res = n + 1
        for j in range(n):
            cur += nums[j]
            while cur >= s:
                res = min(res, j - i + 1)
                cur -= nums[i]
                i += 1

        return 0 if res == (n + 1) else res

    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        accum = [0] * (n + 1)
        for i in range(n):
            accum[i + 1] = accum[i] + nums[i]

        res = n + 1
        for i in range(n):
            right = self.binarySearch(accum, i, n, s + accum[i])
            if right != -1:
                res = min(res, right - i)

        return 0 if res == n + 1 else res

    def binarySearch(self, accum: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (right - left) // 2 + left
            if accum[mid] >= target:
                if mid == left or accum[mid - 1] < target:
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        return -1


if __name__ == '__main__':
    Solution().minSubArrayLen2(7, [2, 3, 1, 2, 4, 3])
