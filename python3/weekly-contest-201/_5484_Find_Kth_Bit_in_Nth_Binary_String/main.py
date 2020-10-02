class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(x):
            y = list()
            for v in x:
                y.append('0' if v == '1' else '1')
            return y

        li = ['0']
        while n > 1:
            r = invert(li)
            li.append('1')
            li.extend(r[::-1])
            n -= 1

        return li[k - 1]
