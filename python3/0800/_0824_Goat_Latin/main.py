class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        res = list()
        for i, w in enumerate(words):
            if w[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                res.append(w + 'ma' + 'a' * (i + 1))
            else:
                res.append(w[1:] + w[0] + 'ma' + 'a' * (i + 1))

        return ' '.join(res)
