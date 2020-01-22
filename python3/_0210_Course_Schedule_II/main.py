from queue import Queue
from typing import List


class Solution:
    # time complexity: O(n + v)
    # space complexity: O(v)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        edges = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            degree[x] += 1
            edges[y].append(x)

        q = Queue()
        res = []

        for i in range(numCourses):
            if not degree[i]:
                q.put(i)

        while not q.empty():
            cur = q.get()
            res.append(cur)
            for x in edges[cur]:
                degree[x] -= 1
                if not degree[x]:
                    q.put(x)

        return res if len(res) == numCourses else []
