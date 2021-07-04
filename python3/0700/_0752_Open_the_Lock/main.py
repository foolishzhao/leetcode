from typing import List


class Solution:
    # corner cases:
    #   1. '0000' in deadends
    #   2. '0000' is target
    def openLock(self, deadends: List[str], target: str) -> int:
        def nextState(x):
            xx = list(x)
            for i, v in enumerate(xx):
                vv = int(v)

                xx[i] = str((vv - 1) % 10)
                yield ''.join(xx)

                xx[i] = str((vv + 1) % 10)
                yield ''.join(xx)

                xx[i] = v

        if target == '0000':
            return 0

        deadends = set(deadends)
        q, seen, res = ['0000'], {'0000'}, 0
        while q:
            nq = list()
            res += 1
            for x in q:
                if x in deadends:
                    continue

                for y in nextState(x):
                    if y == target:
                        return res
                    if y not in seen:
                        nq.append(y)
                        seen.add(y)
            q = nq
        return -1
