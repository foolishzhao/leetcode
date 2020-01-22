package main

import (
	"fmt"
	"sort"
)

func combinationSum2(candidates []int, target int) [][]int {
	sort.Slice(candidates, func(i, j int) bool {
		return candidates[i] < candidates[j]
	})

	res := make([][]int, 0)
	dfs(&res, []int{}, candidates, 0, target)

	return res
}

func dfs(res *[][]int, oneRes []int, nums []int, pos, target int) {
	if target == 0 {
		*res = append(*res, append([]int{}, oneRes...))
		return
	}

	for i := pos; i < len(nums) && target >= nums[i]; i++ {
		if i > pos && nums[i] == nums[i-1] {
			continue
		}

		dfs(res, append(oneRes, nums[i]), nums, i+1, target-nums[i])
	}
}

func main() {
	nums := []int{4, 3, 8, 6, 9}

	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	fmt.Println(nums)
}
