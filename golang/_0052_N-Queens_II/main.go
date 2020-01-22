package main

func totalNQueens(n int) int {
	res := 0
	visited := make([]bool, n)
	dfs([]int{}, visited, &res)

	return res
}

func dfs(nums []int, visited []bool, res *int) {
	if len(nums) == len(visited) {
		*res += 1
		return
	}

	for i := 0; i < len(visited); i++ {
		if !visited[i] && valid(nums, i) {
			visited[i] = true
			dfs(append(nums, i), visited, res)
			visited[i] = false
		}
	}
}

func valid(nums []int, v int) bool {
	n := len(nums)
	for i := 0; i < n; i++ {
		if (n+v == i+nums[i]) || (v-nums[i] == n-i) {
			return false
		}
	}

	return true
}
