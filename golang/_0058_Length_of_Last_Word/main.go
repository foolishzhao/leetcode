package main

func lengthOfLastWord(s string) int {
	res, n := 0, len(s)

	i := n - 1
	for ; i >= 0 && s[i] == ' '; i-- {
	}

	for ; i >= 0 && s[i] != ' '; i-- {
		res++
	}

	return res
}
