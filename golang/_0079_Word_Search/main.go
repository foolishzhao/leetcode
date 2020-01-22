package main

func exist(board [][]byte, word string) bool {
	if len(board) == 0 || len(board[0]) == 0 {
		return false
	}

	m, n := len(board), len(board[0])
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if dfs(board, visited, i, j, word, 0) {
				return true
			}
		}
	}

	return false
}

func dfs(board [][]byte, visited [][]bool, i, j int, word string, pos int) bool {
	if pos == len(word) {
		return true
	}

	m, n := len(board), len(board[0])
	if i >= 0 && i < m && j >= 0 && j < n &&
		board[i][j] == word[pos] && !visited[i][j] {
		visited[i][j] = true
		if dfs(board, visited, i+1, j, word, pos+1) ||
			dfs(board, visited, i-1, j, word, pos+1) ||
			dfs(board, visited, i, j+1, word, pos+1) ||
			dfs(board, visited, i, j-1, word, pos+1) {
			return true
		}
		visited[i][j] = false
	}

	return false
}
