from typing import List
import collections


class Solution:
    # cnt[i] is the maximum count of color i in all paths to the current node.
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, graph = len(colors), collections.defaultdict(list)
        inD = [0] * n

        for u, v in edges:
            graph[u].append(v)
            inD[v] += 1

        q, seen, cnt = list(), 0, [[0] * 26 for _ in range(n)]
        for i in range(n):
            if inD[i] == 0:
                q.append(i)
                cnt[i][ord(colors[i]) - ord('a')] = 1

        res = 0
        while q:
            u = q.pop()
            seen += 1
            res = max(res, max(cnt[u]))
            for v in graph[u]:
                for k in range(26):
                    cnt[v][k] = max(cnt[v][k], cnt[u][k] + (k == (ord(colors[v]) - ord('a'))))
                inD[v] -= 1
                if inD[v] == 0:
                    q.append(v)

        return res if seen == n else -1
