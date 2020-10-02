from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hcuts = sorted([0] + horizontalCuts + [h])
        vcuts = sorted([0] + verticalCuts + [w])

        mh = max([y - x for x, y in zip(hcuts[:-1], hcuts[1:])])
        mv = max([y - x for x, y in zip(vcuts[:-1], vcuts[1:])])
        return (mh * mv) % (10 ** 9 + 7)
