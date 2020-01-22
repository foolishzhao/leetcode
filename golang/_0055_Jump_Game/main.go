package main

func canJump(nums []int) bool {
	n, rightMost := len(nums), 0
	for i := 0; i <= rightMost && rightMost < n-1; i++ {
		rightMost = max(rightMost, i+nums[i])
	}

	return rightMost >= n-1
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
