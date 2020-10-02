from typing import List
import collections


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dt = collections.defaultdict(int)
        for w in wall:
            for i in range(1, len(w)):
                dt[w[i - 1]] += 1
                w[i] += w[i - 1]

        return len(wall) - max(dt.values()) if dt else len(wall)
