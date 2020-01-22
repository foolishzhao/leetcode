package main

func sortColors(nums []int) {
	i, j, k := 0, 0, len(nums)-1
	for j <= k {
		if nums[j] == 0 {
			swap(nums, i, j)
			if i == j {
				j++
			}
			i++
		} else if nums[j] == 1 {
			j++
		} else {
			swap(nums, j, k)
			k--
		}
	}
}

func swap(nums []int, i, j int) {
	nums[i], nums[j] = nums[j], nums[i]
}
