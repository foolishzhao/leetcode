package main

func generateParenthesis(n int) []string {
	res := make([]string, 0)
	if n > 0 {
		dfs(n, 0, 0, &res, "")
	}

	return res
}

func dfs(n, left, right int, res *[]string, curRes string) {
	if left > n {
		return
	} else if right > left {
		return
	} else if left == n && right == n {
		*res = append(*res, curRes)
		return
	} else {
		dfs(n, left+1, right, res, curRes+"(")
		dfs(n, left, right+1, res, curRes+")")
	}
}
