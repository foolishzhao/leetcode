from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
            List[str]:
        q = list()
        q.append(id)

        curLevel = 0
        visited = set(q)
        while curLevel < level:
            sz = len(q)
            for i in range(sz):
                f = q.pop(0)
                for v in friends[f]:
                    if v not in visited:
                        q.append(v)
                        visited.add(v)
            curLevel += 1

        dt = dict()
        for f in q:
            for v in watchedVideos[f]:
                dt[v] = dt.get(v, 0) + 1

        return [x[0] for x in sorted(dt.items(), key=lambda x: (x[1], x[0]))]
