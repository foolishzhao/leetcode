from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen, q = {0}, [0]
        while q:
            idx = q.pop(0)
            for r in rooms[idx]:
                if r not in seen:
                    seen.add(r)
                    q.append(r)
        return len(seen) == len(rooms)
