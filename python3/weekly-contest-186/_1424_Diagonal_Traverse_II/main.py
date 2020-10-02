from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        li = list()
        for i, num in enumerate(nums):
            for j, v in enumerate(num):
                li.append((i, j, v))

        li.sort(key=lambda x: (x[0] + x[1], x[1]))
        return [x[2] for x in li]

    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        li = collections.defaultdict(list)
        for i, num in enumerate(nums):
            for j, v in enumerate(num):
                li[i + j].append(v)

        i, res = 0, list()
        while i in li:
            res.extend(li[i][::-1])
            i += 1
        return res
