class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space = text.count(' ')

        if len(words) == 1:
            return words[0] + ' ' * space
        else:
            a, b = space // (len(words) - 1), space % (len(words) - 1)
            return (' ' * a).join(words) + ' ' * b
