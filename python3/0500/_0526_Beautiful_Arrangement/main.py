import collections


class Solution:
    def __init__(self):
        self.res = 0

    def countArrangement(self, N: int) -> int:
        dt = collections.defaultdict(list)
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i % j == 0 or j % i == 0:
                    dt[i].append(j)

        self.dfs(0, N, dt, set())
        return self.res

    def dfs(self, pos, N, dt, visited):
        if pos == N:
            self.res += 1
            return

        for v in dt[pos + 1]:
            if v not in visited:
                visited.add(v)
                self.dfs(pos + 1, N, dt, visited)
                visited.remove(v)
