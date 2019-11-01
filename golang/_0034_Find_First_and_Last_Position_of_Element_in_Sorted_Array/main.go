package main

func searchRange(nums []int, target int) []int {
	return []int{
		searchFirstPosition(nums, 0, len(nums)-1, target),
		searchLastPosition(nums, 0, len(nums)-1, target),
	}
}

func searchFirstPosition(nums []int, left, right, target int) int {
	if left > right {
		return -1
	}

	mid := (right-left)/2 + left
	if nums[mid] == target {
		if left == mid {
			return mid
		} else {
			return searchFirstPosition(nums, left, mid, target)
		}
	} else if nums[mid] < target {
		return searchFirstPosition(nums, mid+1, right, target)
	} else {
		return searchFirstPosition(nums, left, mid-1, target)
	}
}

func searchLastPosition(nums []int, left, right, target int) int {
	if left > right {
		return -1
	}

	// move right one step 
	mid := (right-left)/2 + left
	if mid+1 <= right {
		mid++
	}

	if nums[mid] == target {
		if mid == right {
			return mid
		} else {
			return searchLastPosition(nums, mid, right, target)
		}
	} else if nums[mid] < target {
		return searchLastPosition(nums, mid+1, right, target)
	} else {
		return searchLastPosition(nums, left, mid-1, target)
	}
}

func main() {
	searchRange([]int{5, 7, 7, 8, 8, 10}, 8)
}
