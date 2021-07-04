from typing import List


class Solution:
    # if any ghosts less or equal far to the target, it can go to the target directly
    # if all ghosts more far to the target, you can go to the target directly, no ghost can catch you, unless it's
    # not more far to the target
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d = abs(target[0]) + abs(target[1])
        for gx, gy in ghosts:
            gd = abs(gx - target[0]) + abs(gy - target[1])
            if gd <= d:
                return False
        return True
