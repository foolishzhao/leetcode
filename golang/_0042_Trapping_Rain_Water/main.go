package main

func trap(height []int) int {
	n, res := len(height), 0
	if n > 2 {
		left := make([]int, n)
		left[1] = height[0]
		for i := 2; i < n; i++ {
			left[i] = max(height[i-1], left[i-1])
		}

		right := make([]int, n)
		right[n-2] = height[n-1]
		for i := n - 3; i >= 0; i-- {
			right[i] = max(right[i+1], height[i+1])
		}

		for i := 1; i < n-1; i++ {
			res += max(min(left[i], right[i])-height[i], 0)
		}
	}

	return res
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

func trap1(height []int) int {
	n, res := len(height), 0
	if n > 2 {
		left := make([]int, n)
		left[1] = height[0]
		for i := 2; i < n; i++ {
			left[i] = max(height[i-1], left[i-1])
		}

		rightLargest := height[n-1]
		for i := n - 2; i > 0; i-- {
			res += max(min(left[i], rightLargest)-height[i], 0)
			rightLargest = max(rightLargest, height[i])
		}
	}

	return res
}

func trap2(height []int) int {
	n, res := len(height), 0
	if n > 2 {
		leftMost, rightMost := height[0], height[n-1]
		for i, j := 1, n-2; i <= j; {
			if leftMost <= rightMost {
				res += max(leftMost-height[i], 0)
				leftMost = max(leftMost, height[i])
				i++
			} else {
				res += max(rightMost-height[j], 0)
				rightMost = max(rightMost, height[j])
				j--
			}
		}
	}

	return res
}
