from typing import List
import heapq


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        curI, curS = [0] * m, sum([mat[i][0] for i in range(m)])
        q = [(curS, curI)]
        visited = {str(curI)}
        while k:
            curS, curI = heapq.heappop(q)
            for i, pos in enumerate(curI):
                if pos + 1 < n:
                    curI[i] += 1
                    strCurI = str(curI)
                    if strCurI not in visited:
                        heapq.heappush(q, (curS - mat[i][pos] + mat[i][pos + 1], curI[:]))
                        visited.add(strCurI)
                    curI[i] -= 1
            k -= 1
        return curS
