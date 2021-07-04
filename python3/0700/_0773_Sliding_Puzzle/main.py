from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        mov = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        seen, s = set(), ''.join([str(c) for row in board for c in row])
        level, q = 0, [(s, s.index('0'))]
        while q:
            nq = list()
            for s, i in q:
                seen.add(s)
                if s == "123450":
                    return level
                sArr = list(s)
                for j in mov[i]:
                    sArr[i], sArr[j] = sArr[j], sArr[i]
                    ns = ''.join(sArr)
                    if ns not in seen:
                        nq.append((ns, j))
                    sArr[i], sArr[j] = sArr[j], sArr[i]
            q = nq
            level += 1
        return -1
