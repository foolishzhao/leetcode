package main

func numDecodings(s string) int {
	n := len(s)
	if n == 0 || s[0] == '0' {
		return 0
	}

	dp := make([]int, n+1)
	dp[0], dp[1] = 1, 1
	for i := 1; i < n; i++ {
		prev, cur := s[i-1], s[i]
		if cur == '0' {
			if prev != '1' && prev != '2' {
				return 0
			}
			dp[i+1] = dp[i-1]
			continue
		}

		if prev == '1' || (prev == '2' && cur <= '6') {
			dp[i+1] = dp[i] + dp[i-1]
		} else {
			dp[i+1] = dp[i]
		}
	}

	return dp[n]
}
