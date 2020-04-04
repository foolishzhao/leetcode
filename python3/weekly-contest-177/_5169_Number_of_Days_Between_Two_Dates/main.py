class Solution:
    def __init__(self):
        self.daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2:
            return self.daysBetweenDates(date2, date1)

        y1, m1, d1 = [int(x) for x in date1.split("-")]
        y2, m2, d2 = [int(x) for x in date2.split("-")]
        days, year = 0, y1
        while year < y2:
            days += self.daysOfYear(year)
            year += 1

        days -= self.daysInYear(y1, m1, d1)
        days += self.daysInYear(y2, m2, d2)

        return days

    def isLeapYear(self, y):
        return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)

    def daysOfYear(self, y):
        days = sum(self.daysOfMonth)
        if self.isLeapYear(y):
            return days + 1
        else:
            return days

    def daysInYear(self, y, m, d):
        days = 0
        for i in range(m - 1):
            days += self.daysOfMonth[i]
            if i == 1 and self.isLeapYear(y):
                days += 1

        return days + d


if __name__ == '__main__':
    obj = Solution()
    print(obj.daysBetweenDates("1971-06-29", "2010-09-23"))
