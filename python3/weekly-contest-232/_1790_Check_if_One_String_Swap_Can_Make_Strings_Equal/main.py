class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt, diff = [0] * 26, 0
        for c1, c2 in zip(s1, s2):
            diff += c1 != c2
            cnt[ord(c1) - ord('a')] += 1
            cnt[ord(c2) - ord('a')] -= 1
        return not diff or (diff == 2 and not any(cnt))

    def areAlmostEqual2(self, s1: str, s2: str) -> bool:
        diff = [[c1, c2] for c1, c2 in zip(s1, s2) if c1 != c2]
        return not diff or (len(diff) == 2 and diff[0] == diff[1][::-1])
