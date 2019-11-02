package main

func solveSudoku(board [][]byte) {
	solveSudokuHelper(board, 0)
}

func solveSudokuHelper(board [][]byte, n int) bool {
	if n == 81 {
		return true
	}

	row, col := n/9, n%9
	if board[row][col] != '.' {
		return solveSudokuHelper(board, n+1)
	} else {
		for c := byte('1'); c <= byte('9'); c++ {
			if isValid(board, row, col, c) {
				board[row][col] = c
				if solveSudokuHelper(board, n+1) {
					return true
				}
				// if deeper invoke returns false, board will be dirty
				board[row][col] = '.'
			}
		}

		return false
	}
}

func isValid(board [][]byte, row, col int, c byte) bool {
	for i := 0; i < 9; i++ {
		if c == board[row][i] {
			return false
		}
	}

	for i := 0; i < 9; i++ {
		if c == board[i][col] {
			return false
		}
	}

	m, n := row/3*3, col/3*3
	for i := m; i < m+3; i++ {
		for j := n; j < n+3; j++ {
			if c == board[i][j] {
				return false
			}
		}
	}

	return true
}

func main() {
	board := [][]byte{
		{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
		{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
		{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
		{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
		{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
		{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
		{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
		{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
		{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
	}
	solveSudoku(board)
}
