from typing import List


class Solution:
    # All the elements in set is non-increasing by flipping 1 bits to 0 from arr[i].
    # Since there are at most 32 1s in arr[i].
    # Thus the size of the set is <= 32.
    def closestToTarget(self, arr: List[int], target: int) -> int:
        prev, res = set(), float('inf')
        for num in arr:
            cur = {num}
            for v in prev:
                cur.add(v & num)

            for v in cur:
                res = min(res, abs(v - target))

            prev = cur

        return res
