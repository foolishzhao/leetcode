from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageScore = sorted([(age, score) for age, score in zip(ages, scores)])
        n = len(scores)
        dp = [0] * n
        for i in range(n):
            dp[i] = ageScore[i][1]
            for j in range(0, i):
                if ageScore[j][1] <= ageScore[i][1]:
                    dp[i] = max(dp[i], dp[j] + ageScore[i][1])

        return max(dp)
