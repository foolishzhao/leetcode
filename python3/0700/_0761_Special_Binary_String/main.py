class Solution:
    # Think of it as Valid-Parentheses
    def makeLargestSpecial(self, S: str) -> str:
        count, i = 0, 0
        subs = list()
        for j, c in enumerate(S):
            count += 1 if c == '1' else -1
            if count == 0:
                subs.append('1' + self.makeLargestSpecial(S[i + 1: j]) + '0')
                i = j + 1
        return ''.join(sorted(subs, reverse=True))
