class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y, visited = 0, 0, {(0, 0)}
        for mov in path:
            if mov == 'N':
                y += 1
            elif mov == 'S':
                y -= 1
            elif mov == 'E':
                x -= 1
            else:
                x += 1

            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
