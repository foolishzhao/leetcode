class Solution:
    """
    Given the string s, the greedy choice is the smallest s[i], s.t.
    the suffix s[i .. ] contains all the unique letters.
    When there are more than one smallest s[i]'s, choose the leftmost one. Consider the case: abcacb
    """

    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return s

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        idx = 0
        for i, c in enumerate(s):
            if c < s[idx]:
                idx = i
            cnt[ord(c) - ord('a')] -= 1
            if not cnt[ord(c) - ord('a')]:
                break

        return s[idx] + self.removeDuplicateLetters(s[idx:].replace(s[idx], ""))

    def removeDuplicateLetters2(self, s: str) -> str:
        res = ""
        while s:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1

            idx = 0
            for i, c in enumerate(s):
                if c < s[idx]:
                    idx = i
                cnt[ord(c) - ord('a')] -= 1
                if not cnt[ord(c) - ord('a')]:
                    break
            res += s[idx]
            s = s[idx:].replace(s[idx], "")

        return res
