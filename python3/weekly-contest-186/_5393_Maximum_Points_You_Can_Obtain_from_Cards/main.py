from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints) - k
        msMin = curSum = sum(cardPoints[:l])
        for i in range(k):
            curSum -= cardPoints[i]
            curSum += cardPoints[i + l]
            msMin = min(msMin, curSum)
        return sum(cardPoints) - msMin
