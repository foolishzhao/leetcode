package main

func removeDuplicates(nums []int) int {
	n, i := len(nums), 1
	if n <= 2 {
		return n
	}

	for j := 2; j < n; j++ {
		if nums[j] > nums[i-1] {
			i++
			nums[i] = nums[j]
		}
	}

	return i + 1
}
