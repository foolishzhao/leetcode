from typing import List


class Solution:
    def longestConsecutive2(self, nums: List[int]) -> int:
        longest, s = 0, set(nums)
        for num in nums:
            cur_longest, j = 1, 1
            while num - j in s: 
                s.remove(num - j)
                cur_longest, j = cur_longest + 1, j + 1
            j = 1
            while num + j in s: 
                s.remove(num + j)
                cur_longest, j = cur_longest + 1, j + 1
            longest = max(longest, cur_longest)
        return longest
    def longestConsecutive(self, nums):
        s, longest = set(nums), 0
        for num in s:
            if num - 1 in s: continue
            j = 1
            while num + j in s: j += 1
            longest = max(longest, j)
        return longest
