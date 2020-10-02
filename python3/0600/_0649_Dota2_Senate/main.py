class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rk, dk = 0, 0
        while True:
            ns = ""
            for s in senate:
                if s == 'R':
                    if rk:
                        rk -= 1
                    else:
                        ns += 'R'
                        dk += 1
                else:
                    if dk:
                        dk -= 1
                    else:
                        ns += 'D'
                        rk += 1
            if senate == ns:
                break
            senate = ns
        return "Radiant" if senate[0] == 'R' else "Dire"

    def predictPartyVictory2(self, senate: str) -> str:
        qr, qd = list(), list()
        for i, s in enumerate(senate):
            if s == 'R':
                qr.append(i)
            else:
                qd.append(i)

        n = len(senate)
        while qr and qd:
            r, d = qr.pop(0), qd.pop(0)
            if r < d:
                qr.append(r + n)
            else:
                qd.append(d + n)

        return "Radiant" if qr else "Dire"
