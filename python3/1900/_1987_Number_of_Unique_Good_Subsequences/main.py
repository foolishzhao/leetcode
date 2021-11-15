class Solution:
    # ends0: # of seq ends with 0, not including 0 itself
    # ends1: # of seq ends with 1
    # consider single 0 separately
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        ends0, ends1, has0 = 0, 0, 0
        for b in binary:
            if b == '0':
                ends0 = ends0 + ends1  # original ends0 is included in new ends0 + ends1 seqs
                has0 = 1
            else:
                ends1 = ends0 + ends1 + 1  # original ends1 is included in new ends0 + ends1 seqs, plus single 1
        return (ends0 + ends1 + has0) % (10 ** 9 + 7)
