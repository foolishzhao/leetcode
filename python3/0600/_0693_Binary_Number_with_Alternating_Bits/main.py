class Solution:
    def __init__(self):
        def addCandidates(x):
            y = x
            while y < (1 << 32):
                self.candidates.add(y)
                y = (y << 2) | x

        self.candidates = set()
        addCandidates(1)
        addCandidates(2)

    def hasAlternatingBits(self, n: int) -> bool:
        return n in self.candidates

    def hasAlternatingBits2(self, n: int) -> bool:
        bs = bin(n)
        return '00' not in bs and '11' not in bs
