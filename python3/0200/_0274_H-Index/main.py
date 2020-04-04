from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        citations.sort()
        n = len(citations)

        for i in range(n):
            if citations[i] >= n - i:
                return n - i

        return 0
