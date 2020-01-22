package main

func minPathSum(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}

	m, n := len(grid), len(grid[0])

	for i := 1; i < m; i++ {
		grid[i][0] += grid[i-1][0]
	}

	for i := 1; i < n; i++ {
		grid[0][i] += grid[0][i-1]
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			grid[i][j] += min(grid[i-1][j], grid[i][j-1])
		}
	}

	return grid[m-1][n-1]
}

func minPathSum2(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}

	m, n := len(grid), len(grid[0])
	prev := make([]int, n+1)
	now := make([]int, n+1)

	for i := 1; i <= n; i++ {
		prev[i] = grid[0][i-1] + prev[i-1]
	}

	for i := 1; i < m; i++ {
		for j := 1; j <= n; j++ {
			if j == 1 {
				now[j] = grid[i][j-1] + prev[j]
			} else {
				now[j] = grid[i][j-1] + min(prev[j], now[j-1])
			}
		}

		prev, now = now, prev
		for j := 0; j <= n; j++ {
			now[j] = 0
		}
	}

	return prev[n]
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
