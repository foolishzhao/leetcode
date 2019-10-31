package main

func removeElement(nums []int, val int) int {
	i, j, n := 0, 0, len(nums)
	for ; j < n; j++ {
		if nums[j] != val {
			nums[i] = nums[j]
			i++
		}
	}

	return i
}
