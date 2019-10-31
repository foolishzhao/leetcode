package main

import "sort"

func fourSum(nums []int, target int) [][]int {
	n, res := len(nums), make([][]int, 0)
	if n >= 4 {
		sort.Ints(nums)
		for i := 0; i < n-3; i++ {
			if i > 0 && nums[i] == nums[i-1] {
				continue
			}

			for j := i + 1; j < n-2; j++ {
				if j > i+1 && nums[j] == nums[j-1] {
					continue
				}

				for m, n := j+1, n-1; m < n; {
					sum := nums[i] + nums[j] + nums[m] + nums[n]
					if sum == target {
						res = append(res, []int{nums[i], nums[j], nums[m], nums[n]})
						m++
						for m < n && nums[m] == nums[m-1] {
							m++
						}
					} else if sum < target {
						m++
					} else {
						n--
					}
				}
			}
		}
	}

	return res
}
