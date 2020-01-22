package main

func jump(nums []int) int {
	res, rightMost, edge := 0, 0, 0
	for i := 0; i < len(nums)-1; i++ {
		rightMost = max(rightMost, i+nums[i])
		if i == edge {
			res++
			edge = rightMost
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
