from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i, t in enumerate(tickets):
            if t < tickets[k]:
                res += t
            else:
                res += tickets[k] if i <= k else tickets[k] - 1
        return res
