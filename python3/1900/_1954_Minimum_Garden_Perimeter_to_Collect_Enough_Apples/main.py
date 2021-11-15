class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        apples, side, x = 12, 2, 1
        while apples < neededApples:
            side += 2
            x += 1
            apples += ((side + x + 1) * (side - x) // 2 + (side - 1 + x) * (side - x) // 2) * 4

        return side * 4

    def minimumPerimeter2(self, neededApples: int) -> int:
        # Num apples per quadrant: (x + 3) * x // 2 + (x + 5) * x // 2 + ... + (x + 2x + 1) * x // 2 = x^3 + x^2
        # Num apples on per x & y axes: x * (x + 1) // 2
        def count(x):
            return (x ** 3 + x ** 2) * 4 + (x * (x + 1) // 2) * 4

        lo, hi = 1, 1000000
        while lo <= hi:
            mi = (lo + hi) // 2
            if count(mi) >= neededApples:
                if mi == lo or count(mi - 1) < neededApples:
                    return mi * 8
                hi = mi - 1
            else:
                lo = mi + 1

        return lo * 8
