import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        dt = collections.defaultdict(int)
        for c in s:
            dt[c] += 1

        for c, cnt in dt.items():
            if cnt < k:
                return max(self.longestSubstring(x, k) for x in s.split(c))

        return len(s)

    def longestSubstring2(self, s: str, k: int) -> int:
        res, n = 0, len(s)
        for t in range(1, 27):
            count = [0] * 26
            i, j, uniq = 0, 0, 0
            while j < n:
                idx = ord(s[j]) - ord('a')
                if count[idx] == 0:
                    uniq += 1
                count[idx] += 1

                while uniq > t:
                    count[ord(s[i]) - ord('a')] -= 1
                    if count[ord(s[i]) - ord('a')] == 0:
                        uniq -= 1
                    i += 1

                if uniq == t:
                    valid = True
                    for c in count:
                        if 0 < c < k:
                            valid = False

                    if valid:
                        res = max(res, j - i + 1)
                j += 1

        return res
