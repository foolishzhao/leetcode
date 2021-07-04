import collections


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        dt = collections.defaultdict(int)
        for i, c in enumerate(list(order)):
            dt[c] = i

        return ''.join(sorted(list(str), key=lambda x: dt[x]))
