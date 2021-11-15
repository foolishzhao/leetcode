from typing import List
import collections


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        dt = collections.defaultdict(int)
        for x in hand:
            dt[x] += 1

        hand.sort()
        while hand:
            k, x = groupSize, hand[0]
            for y in range(groupSize):
                if dt[x + y] <= 0:
                    return False
                dt[x + y] -= 1
                hand.remove(x + y)
        return True

    def isNStraightHand2(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        dt = collections.defaultdict(int)
        for x in hand:
            dt[x] += 1

        for x in sorted(dt.keys()):
            if dt[x] > 0:
                diff = dt[x]
                for j in range(groupSize):
                    if dt[x + j] - diff < 0:
                        return False
                    dt[x + j] -= diff
        return True
