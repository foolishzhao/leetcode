from typing import List

"""
lets start with two points:
a--------------------------------b
the smallest moves is any point between a and b, and the number of moves is b-a

if we add another two points
a--------c----------d------------b
what's the minimum moves to make sure c and d make the smallest number of moves?
it the same logic as a and b, which is any point between c and d.

if elem cnt in nums is even, target point is any point between two median nums, else it's median num.
"""


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        m = nums[len(nums) // 2]
        return sum(abs(x - m) for x in nums)
