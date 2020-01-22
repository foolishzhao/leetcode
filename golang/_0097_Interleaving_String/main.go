package main

func isInterleave(s1 string, s2 string, s3 string) bool {
	if len(s1)+len(s2) != len(s3) {
		return false
	}

	n1, n2 := len(s1), len(s2)
	dp := make([][]bool, n1+1)
	for i := 0; i <= n1; i++ {
		dp[i] = make([]bool, n2+1)
	}

	dp[0][0] = true

	for i := 1; i <= n1; i++ {
		if s1[i-1] == s3[i-1] && dp[i-1][0] {
			dp[i][0] = true
		} else {
			break
		}
	}

	for i := 1; i <= n2; i++ {
		if s2[i-1] == s3[i-1] && dp[0][i-1] {
			dp[0][i] = true
		} else {
			break
		}
	}

	for i := 1; i <= n1; i++ {
		for j := 1; j <= n2; j++ {
			if (s1[i-1] == s3[i+j-1] && dp[i-1][j]) ||
				(s2[j-1] == s3[i+j-1] && dp[i][j-1]) {
				dp[i][j] = true
			}
		}
	}

	return dp[n1][n2]
}
