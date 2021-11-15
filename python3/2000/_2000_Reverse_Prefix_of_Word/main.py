class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            idx = word.find(ch)
            word = word[:idx + 1][::-1] + word[idx + 1:]
        return word
