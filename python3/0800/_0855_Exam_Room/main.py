import bisect


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seats = list()

    def seat(self) -> int:
        res = 0
        if self.seats:
            d = self.seats[0]
            for prev, cur in zip(self.seats, self.seats[1:]):
                if (cur - prev) // 2 > d:
                    d = (cur - prev) // 2
                    res = prev + d
            if self.n - 1 - self.seats[-1] > d:
                res = self.n - 1

        bisect.insort(self.seats, res)
        return res

    def leave(self, p: int) -> None:
        self.seats.remove(p)
