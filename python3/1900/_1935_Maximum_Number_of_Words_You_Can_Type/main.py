class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken, res = set(brokenLetters), 0
        for w in text.split():
            r = 1
            for c in w:
                if c in broken:
                    r = 0
                    break
            res += r
        return res

    def canBeTypedWords2(self, text: str, brokenLetters: str) -> int:
        broken, res = set(brokenLetters), 0
        for w in text.split():
            res += all([c not in broken for c in w])
        return res
