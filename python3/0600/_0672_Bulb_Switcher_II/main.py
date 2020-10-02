class Solution:
    # as every op can take effect at most once, iterate 4 round is enough to get all possible results
    def flipLights(self, n: int, m: int) -> int:
        def op1(lights):
            return [1 - v for v in lights]

        def op2(lights):
            return [v if i % 2 == 0 else (1 - v) for i, v in enumerate(lights)]

        def op3(lights):
            return [v if i % 2 == 1 else (1 - v) for i, v in enumerate(lights)]

        def op4(lights):
            return [(1 - v) if i % 3 == 0 else v for i, v in enumerate(lights)]

        if not m or not n:
            return 1

        candidate = [[1] * n]
        for _ in range(min(m, 4)):
            cur = list()
            for c in candidate:
                cur.append(op1(c))
                cur.append(op2(c))
                cur.append(op3(c))
                cur.append(op4(c))
            candidate = cur  # replace, not extend

        return len({str(c) for c in candidate})


if __name__ == '__main__':
    Solution().flipLights(2, 1)
