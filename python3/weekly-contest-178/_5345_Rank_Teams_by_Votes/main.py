from typing import List
import collections


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = collections.defaultdict(lambda: [0] * len(votes[0]))
        for vote in votes:
            for r, t in enumerate(vote):
                teams[t][r] += 1

        teams = sorted(teams.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
        return ''.join(x[0] for x in teams)
