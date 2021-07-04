from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] != newColor:
            m, n, oc = len(image), len(image[0]), image[sr][sc]
            q = [(sr, sc)]
            while q:
                r, c = q.pop(0)
                if 0 <= r < m and 0 <= c < n and image[r][c] == oc:
                    image[r][c] = newColor
                    q.append((r + 1, c))
                    q.append((r - 1, c))
                    q.append((r, c + 1))
                    q.append((r, c - 1))
        return image
