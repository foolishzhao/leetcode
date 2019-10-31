package main

func nextPermutation(nums []int) {
	n := len(nums)
	if n <= 1 {
		return
	}

	i, j := n-1, n-1
	for i > 0 && nums[i] <= nums[i-1] {
		i--
	}

	if i == 0 {
		reverse(nums)
	} else {
		for nums[j] <= nums[i-1] {
			j--
		}
		swap(nums, i-1, j)
		reverse(nums[i:])
	}
}

func reverse(nums []int) {
	for i, j := 0, len(nums)-1; i < j; i, j = i+1, j-1 {
		swap(nums, i, j)
	}
}

func swap(nums []int, i, j int) {
	nums[i], nums[j] = nums[j], nums[i]
}
