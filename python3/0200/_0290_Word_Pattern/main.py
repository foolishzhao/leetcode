class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(pattern) != len(words):
            return False

        dt = dict()
        for i, p in enumerate(pattern):
            if p in dt and dt[p] != words[i]:
                return False

            if p not in dt and words[i] in dt.values():
                return False

            dt[p] = words[i]

        return True
