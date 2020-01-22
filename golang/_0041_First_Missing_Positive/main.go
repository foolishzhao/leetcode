package main

func firstMissingPositive(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 1
	}

	for i := 0; i < n; {
		if nums[i] >= 1 && nums[i] <= n && nums[i] != nums[nums[i]-1] {
			swap(nums, i, nums[i]-1)
		} else {
			i++
		}
	}

	for i := 0; i < n; i++ {
		if nums[i] != i+1 {
			return i + 1
		}
	}

	return n + 1
}

func swap(nums []int, i, j int) {
	nums[i], nums[j] = nums[j], nums[i]
}
