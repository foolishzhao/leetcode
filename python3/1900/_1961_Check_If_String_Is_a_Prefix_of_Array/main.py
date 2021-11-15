from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i, n = 0, len(words)
        while i < n:
            if s.startswith(words[i]):
                s = s[len(words[i]):]
                if not s:
                    break
            else:
                return False
            i += 1
        return not s
