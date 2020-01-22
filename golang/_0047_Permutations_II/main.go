package main

import "sort"

func permuteUnique(nums []int) [][]int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	res := make([][]int, 0)
	visited := make([]bool, len(nums))
	dfs(&res, []int{}, nums, visited)

	return res
}

func dfs(res *[][]int, oneRes, nums []int, visited []bool) {
	if len(oneRes) == len(nums) {
		*res = append(*res, append([]int{}, oneRes...))
		return
	}

	for i := 0; i < len(nums); i++ {
		if visited[i] {
			continue
		}

		if i > 0 && nums[i] == nums[i-1] && !visited[i-1] {
			continue
		}

		visited[i] = true
		dfs(res, append(oneRes, nums[i]), nums, visited)
		visited[i] = false
	}
}

func swap(nums []int, i, j int) {
	nums[i], nums[j] = nums[j], nums[i]
}
