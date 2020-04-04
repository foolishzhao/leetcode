class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False

        queue, visited = [(0, 0)], set()
        while queue:
            a, b = queue.pop(0)
            if (a, b) in visited:
                continue

            visited.add((a, b))
            if a + b == z:
                return True

            # fill x
            queue.append((x, b))
            # fill y
            queue.append((a, y))
            # pour x
            queue.append((0, b))
            # pour y
            queue.append((a, 0))
            # pour from y to x
            if a + b <= x:
                queue.append((a + b, 0))
            else:
                queue.append((x, a + b - x))
            # pour from x to y
            if a + b <= y:
                queue.append((0, a + b))
            else:
                queue.append((a + b - y, y))

        return False

    def canMeasureWater2(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False

        return not z or z % self.gcd(x, y) == 0

    def gcd(self, x, y):
        return y if not x else self.gcd(y % x, x)
