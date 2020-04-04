class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for sc, tc in zip(s, t):
            count[ord(sc) - ord('a')] += 1
            count[ord(tc) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False

        return True
