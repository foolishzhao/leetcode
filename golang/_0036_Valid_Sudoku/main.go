package main

func isValidSudoku(board [][]byte) bool {
	m := len(board)
	if m != 9 {
		return false
	}

	n := len(board[0])
	if n != 9 {
		return false
	}

	for i := 0; i < 9; i++ {
		set := make(map[byte]bool, 9)
		for j := 0; j < 9; j++ {
			if !validHelper(set, board[i][j]) {
				return false
			}
		}
	}

	for i := 0; i < 9; i++ {
		set := make(map[byte]bool, 9)
		for j := 0; j < 9; j++ {
			if !validHelper(set, board[j][i]) {
				return false
			}
		}
	}

	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			set := make(map[byte]bool, 9)
			for m := 0; m < 3; m++ {
				for n := 0; n < 3; n++ {
					if !validHelper(set, board[i*3+m][j*3+n]) {
						return false
					}
				}
			}
		}
	}

	return true
}

func validHelper(set map[byte]bool, c byte) bool {
	if c != '.' {
		if set[c] {
			return false
		}

		set[c] = true
	}

	return true
}
