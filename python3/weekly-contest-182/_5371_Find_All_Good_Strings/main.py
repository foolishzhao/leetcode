import functools


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        nxt = self.getNext(evil)

        @functools.lru_cache(None)
        def dfs(pos, pre1, pre2, preE):
            if preE == len(evil):
                return 0

            if pos == n:
                return 1

            sc = s1[pos] if pre1 else 'a'
            ec = s2[pos] if pre2 else 'z'
            res = 0
            for v in range(ord(sc), ord(ec) + 1):
                c = chr(v)
                nPre1 = pre1 and c == sc
                nPre2 = pre2 and c == ec
                nPreE = preE
                while nPreE and evil[nPreE] != c:
                    nPreE = nxt[nPreE]

                if evil[nPreE] == c:
                    nPreE += 1

                res += dfs(pos + 1, nPre1, nPre2, nPreE)
                res %= 10 ** 9 + 7

            return res

        return dfs(0, True, True, 0)

    def getNext(self, s):
        n, i, j = len(s), 0, 1
        nxt = [0] * (n + 1)

        while j < n:
            if s[i] == s[j]:
                i += 1
                j += 1
                nxt[j] = i
            elif i > 0:
                i = nxt[i]
            else:
                j += 1

        return nxt
