from typing import List
import heapq


class Solution:
    # proof by mathematical induction
    # assume with k courses after sort, we get the optimum candidates
    # for the k + 1 course
    #   if plus its t won't exceed deadline, then add it to candidates, it's the optimum
    #   if plus its t exceed deadline, then we should remove at least one, remove the longest is the optimum
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        totalDuration = 0
        pq = list()
        for c in courses:
            totalDuration += c[0]
            heapq.heappush(pq, -c[0])
            if totalDuration > c[1]:
                totalDuration += heapq.heappop(pq)
        return len(pq)
