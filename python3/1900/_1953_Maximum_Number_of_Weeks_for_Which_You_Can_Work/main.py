from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        sm, mx = sum(milestones), max(milestones)
        if mx <= (sm + 1) // 2:
            return sm
        else:
            return 2 * (sm - mx) + 1
