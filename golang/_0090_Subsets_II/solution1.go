package main

import "sort"

func subsetsWithDup(nums []int) [][]int {
	res := make([][]int, 0)
	if len(nums) > 0 {
		sort.Slice(nums, func(i, j int) bool {
			return nums[i] < nums[j]
		})

		dfs(&res, []int{}, nums, 0)
	}

	return res
}

func dfs(res *[][]int, oneRes []int, nums []int, pos int) {
	*res = append(*res, append([]int{}, oneRes...))

	for i := pos; i < len(nums); i++ {
		if i > pos && nums[i] == nums[i-1] {
			continue
		}

		dfs(res, append(oneRes, nums[i]), nums, i+1)
	}
}
