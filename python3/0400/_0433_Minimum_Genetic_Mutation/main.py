from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        bank.discard(start)

        res, q = 0, [start]
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.pop(0)
                if cur == end:
                    return res

                for i, v in enumerate(cur):
                    for c in ['A', 'C', 'G', 'T']:
                        if v != c:
                            nxt = cur[:i] + c + cur[i + 1:]
                            if nxt in bank:
                                q.append(nxt)
                                bank.discard(nxt)

            res += 1

        return -1


if __name__ == '__main__':
    Solution().minMutation(
        "AAAACCCC",
        "CCCCCCCC",
        ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"],
    )
