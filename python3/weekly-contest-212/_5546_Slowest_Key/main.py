from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key, time, n = keysPressed[0], releaseTimes[0], len(releaseTimes)
        for i in range(1, n):
            if releaseTimes[i] - releaseTimes[i - 1] > time:
                key, time = keysPressed[i], releaseTimes[i] - releaseTimes[i - 1]
            if releaseTimes[i] - releaseTimes[i - 1] == time and keysPressed[i] > key:
                key = keysPressed[i]
        return key
