from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range(n):
                image[i][j] ^= 1

        for i, row in enumerate(image):
            image[i] = row[::-1]

        return image
