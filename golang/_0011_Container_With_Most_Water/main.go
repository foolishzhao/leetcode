package main

func maxArea(height []int) int {
	n, res := len(height), 0
	if n >= 2 {
		left, right := 0, n-1

		for left < right {
			h := 0
			if height[left] < height[right] {
				h = height[left]
				left++
			} else {
				h = height[right]
				right--
			}

			res = max(res, h*(right-left+1))
		}
	}

	return res
}

func max(i, j int) int {
	if i > j {
		return i
	} else {
		return j
	}
}
