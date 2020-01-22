package main

func isScramble(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}

	count := make([]int, 256)
	for _, v := range s1 {
		count[v]++
	}

	for _, v := range s2 {
		if count[v] == 0 {
			return false
		}
		count[v]--
	}

	n := len(s1)
	dp := make([][][]bool, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]bool, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]bool, n+1)
		}
	}

	for k := 1; k <= n; k++ {
		for i := 0; i+k <= n; i++ {
			for j := 0; j+k <= n; j++ {
				if k == 1 {
					if s1[i] == s2[j] {
						dp[i][j][k] = true
					}
				} else {
					for t := 1; t < k; t++ {
						if (dp[i][j][t] && dp[i+t][j+t][k-t]) ||
							(dp[i][j+k-t][t] && dp[i+t][j][k-t]) {
							dp[i][j][k] = true
							break
						}
					}
				}
			}
		}
	}

	return dp[0][0][n]
}
