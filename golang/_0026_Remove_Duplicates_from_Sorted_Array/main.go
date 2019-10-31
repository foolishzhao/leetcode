package main

func removeDuplicates(nums []int) int {
	n, i, j := len(nums), 0, 1
	for ; j < n; j++ {
		if nums[j] > nums[i] {
			i++
			nums[i] = nums[j]
		}
	}

	return i + 1
}
