from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)

        refer = list()
        for w in words:
            incl = False
            for r in refer:
                if r.endswith(w):
                    incl = True
                    break
            if not incl:
                refer.append(w)

        return sum([len(r) + 1 for r in refer])
