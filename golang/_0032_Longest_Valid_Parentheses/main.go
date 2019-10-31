package main

import "fmt"

// let dp[i+1] represent the length of longest valid parentheses ends with s[i]
// then if s[i-1] == '(', dp[i+1] = dp[i-1] + 2
//      if s[i-1-dp[i]] == '(', dp[i+1] = dp[i] + 2 + dp[j]
func longestValidParentheses(s string) int {
	var (
		res int
		n   = len(s)
		dp  = make([]int, n+1)
	)

	if n > 1 {
		for i := 1; i < n; i++ {
			if s[i] == ')' {
				if s[i-1] == '(' {
					dp[i+1] = dp[i-1] + 2
				} else {
					j := i - 1 - dp[i]
					if j >= 0 && s[j] == '(' {
						dp[i+1] = dp[i] + 2 + dp[j]
					}
				}
			}

			if dp[i+1] > res {
				res = dp[i+1]
			}
		}
	}

	return res
}

func main() {
	fmt.Println(longestValidParentheses(")()())"))
}
