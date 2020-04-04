from typing import List
import math
import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        d = 2 * math.pi * random.random()
        # intuition: for the random r in [0, 1], sqrt enlarges r, larger r needs more points to make it uniform
        # detail: number of points should be proportional to the area of the circles, so it's proportional to r ^ 2.
        # So Math.random() is actually (PI * r^2) / (PI * R^2). Thus r/R = Math.sqrt(Math.random()).
        # In other words, we generate a random RATIO of the target area relative to the whole circle.
        r = self.r * math.sqrt(random.uniform(0, 1))
        return [self.x + r * math.cos(d), self.y + r * math.sin(d)]
