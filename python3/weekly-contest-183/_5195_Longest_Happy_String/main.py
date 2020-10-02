class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        li = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            li.sort(reverse=True)
            for i in range(2):
                if li[i][0] == 0:
                    return res

                if len(res) < 2 or not (res[-2] == res[-1] == li[i][1]):
                    res += li[i][1]
                    li[i][0] -= 1
                    break
