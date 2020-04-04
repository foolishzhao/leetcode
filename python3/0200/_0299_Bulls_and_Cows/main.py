class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        dt1, dt2 = dict(), dict()

        for sc, gc in zip(secret, guess):
            if sc == gc:
                bull += 1
            else:
                dt1[sc] = dt1.get(sc, 0) + 1
                dt2[gc] = dt2.get(gc, 0) + 1

        for c in dt1:
            cow += min(dt1[c], dt2.get(c, 0))

        return str(bull) + "A" + str(cow) + "B"
