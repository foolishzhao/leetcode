from typing import List
import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        wMax = int(math.sqrt(area))
        for w in range(wMax, 0, -1):
            if area % w == 0:
                return [area // w, w]
