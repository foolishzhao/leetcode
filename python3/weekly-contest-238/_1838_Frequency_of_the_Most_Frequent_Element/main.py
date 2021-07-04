from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        n, res = len(nums), 0
        prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        for i, num in enumerate(nums):
            # 1st idx to prefix[i] - prefix[idx] + k >= (i - idx) * num
            lo, hi = 0, i
            while lo < hi:
                mi = (lo + hi) >> 1
                if prefix[i] - prefix[mi] + k >= (i - mi) * num:
                    if mi == 0 or prefix[i] - prefix[mi - 1] + k < (i - mi + 1) * num:
                        lo = hi = mi
                    else:
                        hi = mi - 1
                else:
                    lo = mi + 1

            res = max(res, i + 1 - lo)
        return res

    def maxFrequency2(self, nums: List[int], k: int) -> int:
        nums.sort()

        n, i, res, cur = len(nums), 0, 0, 0
        for j in range(n):
            cur += nums[j]
            while k + cur < nums[j] * (j - i + 1):
                cur -= nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res
