from typing import List


class Solution:
    # suppose we have n pairs, and sorted arrays are x1, x2, ..., x2n, x1 is the smallest
    # for the x1, assume its pair is (x1, xy), then to achieve max result, xy must be x2
    # proof by contradiction:
    #   if xy is not x2, then for another n - 1 pairs, there must be a pair (x2, xz)
    #   if we exchange x2 and xy, then we can get higher result, which contradicts, so xy must be x2
    # after (x1, x2) is fixed, repeat this process, final pair groups will be by sort sequence
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
