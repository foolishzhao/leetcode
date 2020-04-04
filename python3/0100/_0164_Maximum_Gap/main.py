from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res, n = 0, len(nums)
        mn, mx = min(nums), max(nums)
        # plus one to calc gap
        gap = (mx - mn + 1) / n
        # tuple can't be changed
        bucket = [[None, None]] * n

        for num in nums:
            # index need to be int
            b = int((num - mn) / gap)
            if not bucket[b][0]:
                bucket[b] = [num, num]
            else:
                bucket[b][0] = min(bucket[b][0], num)
                bucket[b][1] = max(bucket[b][1], num)

        prev = bucket[0][1]
        for i in range(1, n):
            if bucket[i][0]:
                res = max(res, bucket[i][0] - prev)
                prev = bucket[i][1]

        return res


if __name__ == '__main__':
    Solution().maximumGap([3, 6, 9, 1])
