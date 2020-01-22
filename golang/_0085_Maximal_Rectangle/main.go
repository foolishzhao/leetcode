package main

func maximalRectangle(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}

	m, n, res := len(matrix), len(matrix[0]), 0
	height := make([]int, n)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == '0' {
				height[j] = 0
			} else {
				height[j] += 1
			}
		}

		res = max(res, maximalRectangleHelper(height))
	}

	return res
}

func maximalRectangleHelper(height []int) int {
	height = append(height, -1)
	stack := make([]int, len(height))
	res, idx := 0, 0
	for i, v := range height {
		for idx > 0 && v < height[stack[idx-1]] {
			if idx == 1 {
				res = max(res, height[stack[idx-1]]*i)
			} else {
				res = max(res, height[stack[idx-1]]*(i-stack[idx-2]-1))
			}
			idx--
		}

		stack[idx] = i
		idx++
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

func maximalRectangle2(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}

	m, n, res := len(matrix), len(matrix[0]), 0
	height := make([]int, n)
	left := make([]int, n)
	right := make([]int, n)
	for i := 0; i < n; i++ {
		right[i] = n - 1
	}

	for i := 0; i < m; i++ {
		lb, rb := 0, n-1

		for j := n - 1; j >= 0; j-- {
			if matrix[i][j] == '0' {
				right[j] = n - 1
				rb = j - 1
			} else {
				right[j] = min(right[j], rb)
			}
		}

		for j := 0; j < n; j++ {
			if matrix[i][j] == '0' {
				height[j] = 0
				left[j] = 0
				lb = j + 1
			} else {
				height[j] += 1
				left[j] = max(left[j], lb)
			}

			res = max(res, height[j]*(right[j]-left[j]+1))
		}
	}

	return res
}
