class UndergroundSystem:

    def __init__(self):
        # {from: {to: list()}}
        self.duration = dict()
        # {id: (from, t1)}
        self.frm = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.frm[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.frm:
            return

        frm, to = self.frm[id][0], stationName
        d = t - self.frm[id][1]

        if frm not in self.duration:
            self.duration[frm] = dict()
        if to not in self.duration[frm]:
            self.duration[frm][to] = list()
        self.duration[frm][to].append(d)

        del self.frm[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        li = self.duration[startStation][endStation]
        return sum(li) / len(li)
