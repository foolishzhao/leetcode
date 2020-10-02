from typing import List
import collections


class Solution:
    # greedy, try to append first because it only results in long sub sequence, no other side effects
    def isPossible(self, nums: List[int]) -> bool:
        remain = collections.Counter(nums)
        endAt = collections.Counter()
        for num in nums:
            if not remain[num]:
                continue

            remain[num] -= 1
            if endAt[num - 1] > 0:
                endAt[num - 1] -= 1
                endAt[num] += 1
            elif remain[num + 1] > 0 and remain[num + 2] > 0:
                remain[num + 1] -= 1
                remain[num + 2] -= 1
                endAt[num + 2] += 1
            else:
                return False
        return True
