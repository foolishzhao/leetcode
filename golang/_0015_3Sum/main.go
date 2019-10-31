package main

import "sort"

func threeSum(nums []int) [][]int {
	res, n := make([][]int, 0), len(nums)
	if n > 2 {
		sort.Ints(nums)
		for i := 0; i < n-2; i++ {
			if i > 0 && nums[i] == nums[i-1] {
				continue
			}

			for j, k := i+1, n-1; j < k; {
				sum := nums[j] + nums[k] + nums[i]
				if sum == 0 {
					res = append(res, []int{nums[i], nums[j], nums[k]})
					j++
					for j < k && nums[j] == nums[j-1] {
						j++
					}
				} else if sum > 0 {
					k--
				} else {
					j++
				}
			}
		}
	}

	return res
}
