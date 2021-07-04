class Solution:
    def reinitializePermutation(self, n: int) -> int:
        li, res = list(range(n)), 0
        while True:
            li = li[::2] + li[1::2]
            res += 1
            if li == list(range(n)):
                break
        return res
