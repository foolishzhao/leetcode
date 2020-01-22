package _0053_Maximum_Subarray

import "math"

func maxSubArray(nums []int) int {
	res, curMax := math.MinInt32, 0
	for i := 0; i < len(nums); i++ {
		curMax = max(nums[i], curMax+nums[i])
		res = max(res, curMax)
	}

	return res
}

func maxSubArray2(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	return maxSubArrayHelper(nums, 0, len(nums)-1)
}

func maxSubArrayHelper(nums []int, left, right int) int {
	if left == right {
		return nums[left]
	}

	mid := (right-left)/2 + left
	a := maxSubArrayHelper(nums, left, mid)
	b := maxSubArrayHelper(nums, mid+1, right)
	c := maxSubArrayCrossHelper(nums, left, right)

	return max(a, max(b, c))
}

func maxSubArrayCrossHelper(nums []int, left, right int) int {
	mid := (right-left)/2 + left
	leftMax, rightMax := math.MinInt32, math.MinInt32

	for cur, i := 0, mid; i >= left; i-- {
		cur += nums[i]
		leftMax = max(leftMax, cur)
	}

	for cur, i := 0, mid+1; i <= right; i++ {
		cur += nums[i]
		rightMax = max(rightMax, cur)
	}

	return leftMax + rightMax
}

func max(x, y int) int {
	if x < y {
		return y
	} else {
		return x
	}
}
