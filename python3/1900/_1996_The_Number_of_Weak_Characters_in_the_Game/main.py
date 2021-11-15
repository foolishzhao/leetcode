from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()

        n = len(properties)
        right = [0] * (n - 1) + [properties[-1][1]]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], properties[i][1])

        res, i = 0, 0
        for j in range(n):
            if properties[j][0] > properties[i][0]:
                res += sum(properties[k][1] < right[j] for k in range(i, j))
                i = j
        return res

    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        res, mx = 0, 0
        for _, y in properties:
            res += y < mx
            mx = max(mx, y)
        return res
