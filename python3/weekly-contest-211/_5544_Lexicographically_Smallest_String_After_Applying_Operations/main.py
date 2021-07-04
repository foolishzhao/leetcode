class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add(x):
            arr = [int(y) for y in list(x)]
            for i, v in enumerate(arr):
                if i % 2 == 1:
                    arr[i] = (v + a) % 10
            return ''.join([str(y) for y in arr])

        def rotate(x):
            return x[-b:] + x[:n - b]

        def dfs(x):
            if x not in visited:
                visited.add(x)
                dfs(add(x))
                dfs(rotate(x))

        visited, n = set(), len(s)
        dfs(s)
        return min(visited)
