package main

func combine1(n int, k int) [][]int {
	res := make([][]int, 0)
	if n < k || k <= 0 {
		return res
	} else if k == 1 {
		for i := 1; i <= n; i++ {
			res = append(res, []int{i})
		}
	} else if n == k {
		oneRes := make([]int, 0, n)
		for i := n; i >= 1; i-- {
			oneRes = append(oneRes, i)
		}
		res = append(res, oneRes)
	} else {
		r1 := combine1(n-1, k-1)
		for i := range r1 {
			res = append(res, append([]int{n}, r1[i]...))
		}

		r2 := combine1(n-1, k)
		res = append(res, r2...)
	}

	return res
}

func combine(n int, k int) [][]int {
	res := make([][]int, 0)
	dfs(&res, []int{}, n, k)

	return res
}

func dfs(res *[][]int, oneRes []int, n, k int) {
	if len(oneRes) == k {
		*res = append(*res, append([]int{}, oneRes...))
		return
	}

	if n > 0 {
		dfs(res, oneRes, n-1, k)
		dfs(res, append(oneRes, n), n-1, k)
	}
}

func main() {
	combine(5, 4)
}
