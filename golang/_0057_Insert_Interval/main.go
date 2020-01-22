package main

func insert(intervals [][]int, newInterval []int) [][]int {
	res := make([][]int, 0)
	n := len(intervals)
	if n == 0 {
		res = append(res, newInterval)
	} else if newInterval[1] < intervals[0][0] {
		res = append(res, newInterval)
		res = append(res, intervals...)
	} else if newInterval[0] > intervals[n-1][1] {
		res = append(res, intervals...)
		res = append(res, newInterval)
	} else {
		i := 0
		for ; i < n && intervals[i][1] < newInterval[0]; i++ {
			res = append(res, intervals[i])
		}

		newInterval[0] = min(newInterval[0], intervals[i][0])
		for ; i < n && newInterval[1] >= intervals[i][0]; i++ {
			newInterval[1] = max(newInterval[1], intervals[i][1])
		}
		res = append(res, newInterval)

		for ; i < n; i++ {
			res = append(res, intervals[i])
		}
	}

	return res
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
