package main

func largestRectangleArea(heights []int) int {
	heights = append(heights, -1)

	n, res := len(heights), 0
	stack := make([]int, n)
	stackIdx := 0
	for i, v := range heights {
		for stackIdx > 0 && v < heights[stack[stackIdx-1]] {
			if stackIdx == 1 {
				res = max(res, heights[stack[stackIdx-1]]*i)
			} else {
				res = max(res, heights[stack[stackIdx-1]]*(i-stack[stackIdx-2]-1))
			}

			stackIdx--
		}

		stack[stackIdx] = i
		stackIdx++
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

func main() {
	largestRectangleArea([]int{2, 1, 2})
}
