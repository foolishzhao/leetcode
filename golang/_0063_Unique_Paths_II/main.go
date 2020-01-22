package main

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if len(obstacleGrid) == 0 || len(obstacleGrid[0]) == 0 {
		return 0
	}

	m, n := len(obstacleGrid), len(obstacleGrid[0])
	prev := make([]int, n+1)
	now := make([]int, n+1)

	prev[1] = 1
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if obstacleGrid[i-1][j-1] == 0 {
				now[j] = now[j-1] + prev[j]
			}
		}

		prev, now = now, prev
		for j := 0; j <= n; j++ {
			now[j] = 0
		}
	}

	return prev[n]
}
