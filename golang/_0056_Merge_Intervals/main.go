package main

import "sort"

func merge(intervals [][]int) [][]int {
	res := make([][]int, 0)
	if len(intervals) > 0 {
		sort.Slice(intervals, func(i, j int) bool {
			return intervals[i][0] < intervals[j][0]
		})

		n := len(intervals)
		for i := 0; i < n; {
			start, end, j := intervals[i][0], intervals[i][1], i+1
			for j < n {
				if end >= intervals[j][0] {
					end = max(end, intervals[j][1])
					j++
				} else {
					break
				}
			}

			res = append(res, []int{start, end})
			i = j
		}
	}

	return res
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
