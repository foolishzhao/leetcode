class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        sh, sm = startTime.split(':')
        fh, fm = finishTime.split(':')

        ts, tf = int(sh) * 60 + int(sm), int(fh) * 60 + int(fm)
        tf += (ts > tf) * 24 * 60

        return tf // 15 - (ts + 14) // 15
