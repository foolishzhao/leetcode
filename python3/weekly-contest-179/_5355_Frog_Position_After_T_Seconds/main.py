import collections
from typing import List


class Solution:
    def __init__(self):
        self.dt = collections.defaultdict(dict)

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        neighbors = collections.defaultdict(list)
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)

        self.dfs(neighbors, 1, 1.0, 0, set())
        return self.dt[t][target] if t in self.dt and target in self.dt[t] else 0

    def dfs(self, neighbors, x, prob, t, visited):
        visited.add(x)

        if x not in self.dt[t]:
            self.dt[t][x] = 0
        self.dt[t][x] += prob

        nn = 0
        for y in neighbors[x]:
            if y not in visited:
                nn += 1

        if not nn:
            for tt in range(t + 1, 51):
                self.dt[tt][x] = self.dt[t][x]

        for y in neighbors[x]:
            if y not in visited:
                self.dfs(neighbors, y, prob / nn, t + 1, visited)

        visited.remove(x)


# treat graph as a tree, because it has exact n - 1 edges
class Solution2:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        visited, prob = [False] * n, [0] * n
        prob[0] = 1
        q = [0]
        while q and t:
            sz = len(q)
            for _ in range(sz):
                x = q.pop(0)
                visited[x] = True

                childCnt = sum(1 for y in graph[x] if not visited[y])
                for y in graph[x]:
                    if not visited[y]:
                        q.append(y)
                        prob[y] = prob[x] / childCnt

                if childCnt > 0:
                    prob[x] = 0

            t -= 1

        return prob[target - 1]


if __name__ == '__main__':
    Solution2().frogPosition(
        7,
        [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
        2,
        4,
    )
