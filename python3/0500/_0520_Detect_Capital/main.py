class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())

    def detectCapitalUse2(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
