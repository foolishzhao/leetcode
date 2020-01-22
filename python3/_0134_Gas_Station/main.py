from typing import List


class Solution:
    """
    1.If the total number of gas is bigger than the total number of cost. There must be a solution.
    Prove: If the gas is more than the cost in total, there must be some stations we have enough gas to go
           through them. Let's say they are green stations. So the other stations are red.
           The adjacent stations with same color can be joined together as one.
           Then there must be a red station that can be joined into a precedent green station
           unless there isn't any red station, because the total gas is more than the total cost.
           In other words, all of the stations will join into a green station at last.

    2.If car starts at A and can not reach B. Any station between A and B can not reach B.
    (B is the first station that A can not reach.)
    Prove: In any station between A and B, let's say C. C will have gas left in our tank, if we go from A to
           that station. We can't reach B from A with some gas(may be 0) left in the tank in C,
           so we can't reach B from C with an empty tank.
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n, i, cur = len(gas), 0, 0
        for j in range(n):
            cur += gas[j] - cost[j]
            if cur < 0:
                cur = 0
                i = j + 1

        return i
