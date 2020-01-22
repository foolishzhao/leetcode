from typing import List


class Solution:
    # The root of an MHT has to be the middle point (or two middle points)
    # of the longest path of the tree. So there are at most two roots.

    # Any node that has already been a leaf cannot be the root of a MHT,
    # because its adjacent non-leaf node will always be a better candidate.
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [set() for _ in range(n)]
        for x, y in edges:
            adj[x].add(y)
            adj[y].add(x)

        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)

            nxt = []
            for x in leaves:
                y = adj[x].pop()
                adj[y].remove(x)
                if len(adj[y]) == 1:
                    nxt.append(y)
            leaves = nxt

        return leaves
