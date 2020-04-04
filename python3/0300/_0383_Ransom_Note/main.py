import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dt = collections.defaultdict(int)
        for c in magazine:
            dt[c] += 1

        for c in ransomNote:
            if not dt[c]:
                return False
            dt[c] -= 1

        return True
