import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        n, token = len(s1), 0
        for i, c in enumerate(s2):
            counter[c] -= 1

            if counter[c] >= 0:
                token += 1
                if token == n:
                    return True

            if i >= n - 1:
                pc = s2[i - n + 1]
                counter[pc] += 1
                if counter[pc] > 0:
                    token -= 1
        return False
