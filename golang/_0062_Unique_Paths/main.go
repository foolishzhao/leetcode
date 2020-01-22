package main

func uniquePaths(m int, n int) int {
	if m == 0 || n == 0 {
		return 0
	}

	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}

	dp[0][1] = 1
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
		}
	}

	return dp[m][n]
}

func uniquePaths2(m int, n int) int {
	if m == 0 || n == 0 {
		return 0
	}

	prev := make([]int, n+1)
	now := make([]int, n+1)

	prev[1] = 1
	for j := 1; j <= m; j++ {
		for i := 1; i <= n; i++ {
			now[i] = now[i-1] + prev[i]
		}

		prev, now = now, prev
		for i := 0; i <= n; i++ {
			now[i] = 0
		}
	}

	return prev[n]
}
