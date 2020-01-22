package main

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}

	m, n := len(matrix), len(matrix[0])
	row, col := 0, n-1
	for row < m && col >= 0 {
		if matrix[row][col] == target {
			return true
		} else if matrix[row][col] < target {
			row++
		} else {
			col--
		}
	}

	return false
}

func searchMatrix2(matrix [][]int, target int) bool {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}

	m, n := len(matrix), len(matrix[0])
	left, right := 0, m*n-1
	for left <= right {
		mid := (right-left)/2 + left
		midRow, midCol := mid/n, mid%n
		if matrix[midRow][midCol] == target {
			return true
		} else if matrix[midRow][midCol] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return false
}
