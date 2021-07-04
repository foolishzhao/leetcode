from typing import List
import collections


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def getHashSet(path, windowSize):
            q, h = 10 ** 9 + 7, 0
            p, pe = 100001, 100001 ** (windowSize - 1) % q
            for i in range(windowSize):
                h = (h * p + path[i]) % q

            st, dt = {h}, collections.defaultdict(list)
            dt[h].append(0)
            for i in range(windowSize, len(path)):
                h = ((h - path[i - windowSize] * pe) * p + path[i]) % q
                st.add(h)
                dt[h].append(i - windowSize + 1)

            return st, dt

        def isValid(windowSize):
            st, dt = getHashSet(paths[0], windowSize)
            dts = [dt]
            for path in paths[1:]:
                cSt, cDt = getHashSet(path, windowSize)
                st &= cSt
                dts.append(cDt)
                if not st:
                    return False

            # Collision check
            for h in st:
                nSt = set([tuple(paths[0][idx: idx + windowSize]) for idx in dts[0][h]])
                for i in range(1, len(paths)):
                    nSt &= set([tuple(paths[i][idx: idx + windowSize]) for idx in dts[i][h]])
                    if not nSt:
                        break

                if nSt:
                    return True
            return False

        lo, hi = 1, min([len(path) for path in paths])
        while lo <= hi:
            mi = (lo + hi) // 2
            if isValid(mi):
                lo = mi + 1
            else:
                hi = mi - 1
        return hi
