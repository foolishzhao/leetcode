from typing import List
import collections


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        prev = collections.defaultdict(int)
        for i, v in enumerate(arr):
            prev[v] = arr[i - 1] if i else -1

        for piece in pieces:
            for i, v in enumerate(piece):
                if v not in prev:
                    return False
                if i and prev[v] != piece[i - 1]:
                    return False
        return True
