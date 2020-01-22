package main

func subsets(nums []int) [][]int {
	res := make([][]int, 0)
	dfs(&res, []int{}, nums, 0)

	return res
}

func dfs(res *[][]int, oneRes []int, nums []int, pos int) {
	if pos == len(nums) {
		*res = append(*res, append([]int{}, oneRes...))
		return
	}

	dfs(res, oneRes, nums, pos+1)
	dfs(res, append(oneRes, nums[pos]), nums, pos+1)
}

func subsets2(nums []int) [][]int {
	res := make([][]int, 0)
	dfs2(&res, []int{}, nums, 0)

	return res
}

func dfs2(res *[][]int, oneRes []int, nums []int, pos int) {
	*res = append(*res, append([]int{}, oneRes...))
	for i := pos; i < len(nums); i++ {
		dfs2(res, append(oneRes, nums[i]), nums, i+1)
	}
}