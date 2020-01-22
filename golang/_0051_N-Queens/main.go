package main

func solveNQueens(n int) [][]string {
	res := make([][]string, 0)
	visited := make([]bool, n)
	dfs(&res, []int{}, visited)

	return res
}

func dfs(res *[][]string, oneRes []int, visited []bool) {
	if len(oneRes) == len(visited) {
		t := make([]string, 0, len(oneRes))
		for _, v := range oneRes {
			t = append(t, genStr(v, len(visited)))
		}

		*res = append(*res, t)
		return
	}

	for i := 0; i < len(visited); i++ {
		if !visited[i] && isValid(oneRes, i) {
			visited[i] = true
			dfs(res, append(oneRes, i), visited)
			visited[i] = false
		}
	}
}

func isValid(nums []int, v int) bool {
	n := len(nums)
	for i := 0; i < n; i++ {
		if (i+nums[i] == n+v) || (v-nums[i] == n-i) {
			return false
		}
	}

	return true
}

func genStr(v, n int) string {
	arr := make([]byte, n)
	for i := 0; i < n; i++ {
		arr[i] = '.'
	}

	arr[v] = 'Q'
	return string(arr)
}
