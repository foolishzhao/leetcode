from typing import List
from queue import Queue


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        edges = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            degree[x] += 1
            edges[y].append(x)

        n = 0
        q = Queue()
        for i in range(numCourses):
            if not degree[i]:
                q.put(i)

        while not q.empty():
            i = q.get()
            n += 1
            for j in edges[i]:
                degree[j] -= 1
                if not degree[j]:
                    q.put(j)

        return numCourses == n

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            edges[y].append(x)

        #  0 denotes unvisited
        # -1 denotes under visit
        #  1 denotes visited
        # need this because the graph is directed edge.
        visited = [0] * numCourses
        for i in range(numCourses):
            if not visited[i]:
                if self.hasCycle(edges, visited, i):
                    return False

        return True

    def hasCycle(self, edges, visited, i):
        if visited[i] == -1:
            return True

        if visited[i] == 1:
            return False

        visited[i] = -1
        for j in edges[i]:
            if self.hasCycle(edges, visited, j):
                return True
        visited[i] = 1

        return False
