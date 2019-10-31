package main

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	i, n := 0, len(strs)
	for ; i < len(strs[0]); i++ {
		c, j := strs[0][i], 1
		for ; j < n; j++ {
			if i == len(strs[j]) || c != strs[j][i] {
				break
			}
		}

		if j != n {
			break
		}
	}

	return strs[0][:i]
}
