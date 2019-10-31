package main

// divide by mid index, always have a sorted half,
// if target is within the sorted half, then search that half, else search another half
func search(nums []int, target int) int {
	for left, right := 0, len(nums)-1; left <= right; {
		mid := (right-left)/2 + left
		if nums[mid] == target {
			return mid
		} else if nums[mid] >= nums[left] {
			if nums[left] <= target && target <= nums[mid] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else {
			if nums[mid] <= target && target <= nums[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}

	return -1
}
