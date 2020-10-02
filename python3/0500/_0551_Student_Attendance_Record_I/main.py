class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False

        i, j, n = -1, 0, len(s)
        while j < n:
            if s[j] == 'L':
                if j - i > 2:
                    return False
            else:
                i = j
            j += 1

        return True

    def checkRecord2(self, s: str) -> bool:
        return False if s.count('A') > 1 or 'LLL' in s else True

    def checkRecord3(self, s: str) -> bool:
        return s.count('A') <= 1 and s.find('LLL') == -1
