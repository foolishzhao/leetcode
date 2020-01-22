package main

func permute(nums []int) [][]int {
	res := make([][]int, 0)
	dfs(&res, nums, 0)

	return res
}

func dfs(res *[][]int, nums []int, pos int) {
	if pos == len(nums) {
		*res = append(*res, append([]int{}, nums...))
		return
	}

	for i := pos; i < len(nums); i++ {
		swap(nums, pos, i)
		dfs(res, nums, pos+1)
		swap(nums, pos, i)
	}
}

func swap(nums []int, i, j int) {
	nums[i], nums[j] = nums[j], nums[i]
}
