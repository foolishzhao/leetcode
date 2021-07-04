from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n, res = len(boxes), list()
        for i in range(n):
            res.append(sum([abs(i - j) for j in range(n) if boxes[j] == '1']))
        return res

    def minOperations2(self, boxes: str) -> List[int]:
        n, res = len(boxes), [0] * len(boxes)
        step, cur = 0, 0
        for i, box in enumerate(boxes):
            res[i] = step
            cur += box == '1'
            step += cur

        step, cur = 0, 0
        for i, box in enumerate(reversed(boxes)):
            res[n - 1 - i] += step
            cur += box == '1'
            step += cur

        return res
