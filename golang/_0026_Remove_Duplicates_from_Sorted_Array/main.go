package main

func removeDuplicates(nums []int) int {
	n, i := len(nums), 0
	if n <= 1 {
		return n
	}

	for j := 1; j < n; j++ {
		if nums[j] > nums[i] {
			i++
			nums[i] = nums[j]
		}
	}

	return i + 1
}
