package main

func isMatch(s string, p string) bool {
	sLen, pLen := len(s), len(p)
	dp := make([][]bool, pLen+1)
	for i := 0; i <= pLen; i++ {
		dp[i] = make([]bool, sLen+1)
	}

	dp[0][0] = true
	for i := 1; i <= pLen; i++ {
		if p[i-1] == '*' {
			j := 0
			for ; j <= sLen && !dp[i-1][j]; j++ {
			}

			for ; j <= sLen; j++ {
				dp[i][j] = true
			}
		} else {
			for j := 1; j <= sLen; j++ {
				if dp[i-1][j-1] && (p[i-1] == '?' || p[i-1] == s[j-1]) {
					dp[i][j] = true
				}
			}
		}
	}

	return dp[pLen][sLen]
}

func isMatch2(s string, p string) bool {
	sLen, pLen := len(s), len(p)
	prev := make([]bool, sLen+1)
	now := make([]bool, sLen+1)

	prev[0] = true
	for i := 1; i <= pLen; i++ {
		if p[i-1] == '*' {
			j := 0
			for ; j <= sLen && !prev[j]; j++ {
				now[j] = false
			}

			for ; j <= sLen; j++ {
				now[j] = true
			}
		} else {
			for j := 1; j <= sLen; j++ {
				if prev[j-1] && (p[i-1] == '?' || p[i-1] == s[j-1]) {
					now[j] = true
				}
			}
		}

		prev, now = now, prev
		for j := 0; j <= sLen; j++ {
			now[j] = false
		}
	}

	return prev[sLen]
}

func main() {
	isMatch2("mississippi", "m??*ss*?i*pi")
}
