from typing import List
import random


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.rows = n_rows
        self.cols = n_cols
        self.dt = dict()
        self.start, self.end = 0, self.rows * self.cols - 1

    def flip(self) -> List[int]:
        idx = random.randint(self.start, self.end)
        val = self.dt.get(idx, idx)
        self.dt[idx] = self.dt.get(self.start, self.start)
        self.dt[self.start] = val
        self.start += 1
        return [val // self.cols, val % self.cols]

    def reset(self) -> None:
        self.start = 0
