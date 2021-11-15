class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ds = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k):
            ds = str(sum([int(c) for c in ds]))
        return int(ds)