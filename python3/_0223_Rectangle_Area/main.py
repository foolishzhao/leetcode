class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        overlap = 0

        left = max(A, E)
        right = min(C, G)
        bottom = max(B, F)
        top = min(D, H)

        if right > left and top > bottom:
            overlap = (right - left) * (top - bottom)

        return area1 + area2 - overlap
