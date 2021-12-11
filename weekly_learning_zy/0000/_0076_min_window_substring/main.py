import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sct = collections.defaultdict(int)
        tct = collections.Counter(t)
        i = 0
        match = 0
        tLen = len(t)
        res = ""
        for j, c in enumerate(s):
            sct[c] += 1
            if sct[c] <= tct[c]:
                match += 1
            if match == tLen:
                while match == tLen:
                    sct[s[i]] -= 1
                    if sct[s[i]] < tct[s[i]]:
                        match -= 1
                    i += 1
                if not res or len(res) > j - i + 2:
                    res = s[i - 1:j + 1]
        return res


if __name__ ==  '__main__':
    s = "aADOBECODEBANC"
    t = "ABC"
    ans = Solution().minWindow(s, t)
    print(ans)