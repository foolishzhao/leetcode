import collections


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        counter = collections.defaultdict(int)
        for u, v in zip(s, t):
            counter[u] += 1
            counter[v] -= 1

        if any(counter.values()):
            return False

        s, t = list(s), list(t)
        i, n = 0, len(s)
        tCnt = collections.defaultdict(int)
        tCnt[t[0]] += 1
        for j in range(1, n):
            if t[j] < t[j - 1]:
                sCnt = collections.defaultdict(int)
                match, u, first = 0, i, -1
                while u < n:
                    sCnt[s[u]] += 1
                    if sCnt[s[u]] > tCnt[s[u]]:
                        if first == -1:
                            first = u
                    else:
                        match += 1
                    u += 1
                    if match == j - i:
                        break

                if u > j:
                    s[first: u] = sorted(s[first: u])
                    for v in s[i: j]:
                        tCnt[v] -= 1
                    if any(tCnt.values()):
                        return False

                tCnt = collections.defaultdict(int)
                tCnt[t[j]] += 1
                i = j
            else:
                tCnt[t[j]] += 1

        return True

    # s="xxxxAxxxx" t="Axxxxxxxx"
    # To move A to the most left, the best way is moving A one by one,
    # it requires all the char on the left of A must be greater than A.
    # After that question becomes convert s[1:] to t[1:]
    def isTransformable2(self, s: str, t: str) -> bool:
        if collections.Counter(s) != collections.Counter(t):
            return False

        qS = collections.defaultdict(collections.deque)
        for i, c in enumerate(s):
            qS[c].append(i)

        for c in t:
            idx = qS[c].popleft()
            for i in range(int(c)):
                j = str(i)
                if qS[j] and qS[j][0] < idx:
                    return False

        return True
