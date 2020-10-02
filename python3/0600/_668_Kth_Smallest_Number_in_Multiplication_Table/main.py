class Solution:
    # Continue search when the count(mi) == k, as we want to get min candidate, which must be in Multiplication Table.

    # Proof by contradiction: assume min candidate x isn't in Multiplication Table,
    # then x - 1 will also be a candidate, this contradict that x is min candidate
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(v):
            res = 0
            for i in range(1, m + 1):
                res += min(v // i, n)
            return res

        lo, hi = 1, m * n
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            if count(mi) >= k:
                hi = mi
            else:
                lo = mi + 1
        return lo
