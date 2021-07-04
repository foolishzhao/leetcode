class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        A = [(s, i) for i, s in enumerate(start) if s in ('L', 'R')]
        B = [(e, i) for i, e in enumerate(end) if e in ('L', 'R')]

        if len(A) != len(B):
            return False

        for (s, i), (e, j) in zip(A, B):
            if s != e:
                return False
            if s == 'L':
                if i < j:
                    return False
            if s == 'R':
                if i > j:
                    return False
        return True
