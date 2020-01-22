package main

import "fmt"

func combinationSum(candidates []int, target int) [][]int {
	res := make([][]int, 0)
	dfs(&res, []int{}, candidates, 0, target)

	return res
}

func dfs(res *[][]int, oneRes []int, nums []int, index, target int) {
	if target == 0 {
		*res = append(*res, append([]int{}, oneRes...))
		return
	}

	for i := index; i < len(nums); i++ {
		if target >= nums[i] {
			dfs(res, append(oneRes, nums[i]), nums, i, target-nums[i])
		}
	}
}

func main() {
	fmt.Println(combinationSum([]int{2, 3, 6, 7}, 7))
}
