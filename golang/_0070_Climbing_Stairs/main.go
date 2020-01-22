package main

func climbStairs(n int) int {
	prev, cur := 1, 1
	for i := 1; i < n; i++ {
		prev, cur = cur, prev+cur
	}

	return cur
}
