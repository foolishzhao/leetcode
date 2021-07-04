from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n, res, st = len(cars), [-1] * len(cars), list()
        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            # remove all front cars with bigger speed
            while st and cars[st[-1]][1] >= speed:
                st.pop()

            time = -1
            while st:
                time = (cars[st[-1]][0] - pos) / (speed - cars[st[-1]][1])
                # find the first front cars we can catch up
                if time <= res[st[-1]] or res[st[-1]] == -1:
                    break
                st.pop()

            res[i] = time
            st.append(i)
        return res
