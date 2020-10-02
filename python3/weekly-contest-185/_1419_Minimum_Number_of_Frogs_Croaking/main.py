import collections


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        dt = collections.defaultdict(int)
        res = -1
        for c in croakOfFrogs:
            dt[c] += 1
            if dt['r'] > dt['c'] or dt['o'] > dt['r'] or dt['a'] > dt['o'] or dt['k'] > dt['a']:
                return -1
            if dt['k'] > 0:
                res = max(res, dt['c'])
                dt['c'] -= dt['k']
                dt['r'] -= dt['k']
                dt['o'] -= dt['k']
                dt['a'] -= dt['k']
                dt['k'] -= dt['k']

        return -1 if dt['c'] or dt['r'] or dt['o'] or dt['a'] or dt['k'] else res

    # state machine
    def minNumberOfFrogs2(self, croakOfFrogs: str) -> int:
        state, res = [float('inf')] + [0] * 5, 0
        dt = {'c': 1, 'r': 2, 'o': 3, 'a': 4, 'k': 5}
        for c in croakOfFrogs:
            s = dt[c]
            if state[s - 1] > 0:
                state[s - 1] -= 1
                state[s] += 1
            else:
                return -1
            res = max(res, sum(state[1:5]))

        return -1 if sum(state[1:5]) else res
