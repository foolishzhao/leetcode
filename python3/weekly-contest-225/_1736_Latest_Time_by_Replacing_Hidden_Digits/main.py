class Solution:
    def maximumTime(self, time: str) -> str:
        h, m = time.split(':')
        if h == '??':
            h = '23'
        elif h[0] == '?':
            if h[1] <= '3':
                h = '2' + h[1]
            else:
                h = '1' + h[1]
        elif h[1] == '?':
            if h[0] == '2':
                h = h[0] + '3'
            else:
                h = h[0] + '9'

        if m == '??':
            m = '59'
        elif m[0] == '?':
            m = '5' + m[1]
        elif m[1] == '?':
            m = m[0] + '9'

        return h + ':' + m
