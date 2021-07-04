class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ds = ['L'] + list(dominoes) + ['R']

        i, n = 0, len(ds)
        for j in range(1, n):
            if ds[j] == 'L':
                if ds[i] == 'L':
                    for k in range(i + 1, j):
                        ds[k] = 'L'
                else:
                    u, v = i + 1, j - 1
                    while u < v:
                        ds[u], ds[v] = 'R', 'L'
                        u += 1
                        v -= 1
                i = j
            elif ds[j] == 'R':
                if ds[i] == 'R':
                    for k in range(i + 1, j):
                        ds[k] = 'R'
                i = j

        return ''.join(ds[1:-1])
