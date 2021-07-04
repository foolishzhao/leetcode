class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        l = [poured]
        for _ in range(query_row):
            nl = [0] * (len(l) + 1)
            for i in range(len(l)):
                p = (l[i] - 1) / 2
                if p > 0:
                    nl[i] += p
                    nl[i + 1] += p
            l = nl

        return min(1, l[query_glass])
