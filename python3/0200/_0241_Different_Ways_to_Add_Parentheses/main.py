from typing import List


class Solution:
    # catalan number
    # http://blog.miskcoo.com/2015/07/catalan-number
    # https://zhuanlan.zhihu.com/p/31317307
    # http://people.math.sc.edu/howard/Classes/554b/catalan.pdf
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        for i, v in enumerate(input):
            if v in "+-*":
                lRes = self.diffWaysToCompute(input[:i])
                rRes = self.diffWaysToCompute(input[i + 1:])
                for l in lRes:
                    for r in rRes:
                        if v == '+':
                            res.append(l + r)
                        elif v == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        if not res:
            res.append(int(input))

        return res

    # divide and conquer with memo
    def diffWaysToCompute2(self, input: str) -> List[int]:
        return self.helper(input, {})

    def helper(self, input, memo) -> List[int]:
        if input in memo:
            return memo[input]

        if input.isdigit():
            return [int(input)]

        res = []
        for i, v in enumerate(input):
            if v in "+-*":
                lRes = self.helper(input[:i], memo)
                rRes = self.helper(input[i + 1:], memo)
                for l in lRes:
                    for r in rRes:
                        if v == '+':
                            res.append(l + r)
                        elif v == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        memo[input] = res
        return res
