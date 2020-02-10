class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount, tCount = [0] * 26, [0] * 26
        for sc, tc in zip(s, t):
            sCount[ord(sc) - ord('a')] += 1
            tCount[ord(tc) - ord('a')] += 1

        sameCount = 0
        for sc, tc in zip(sCount, tCount):
            sameCount += min(sc, tc)

        return len(s) - sameCount
