package main

func fullJustify(words []string, maxWidth int) []string {
	res := make([]string, 0)
	i, j, n := 0, 0, len(words)
	for i < n {
		var curWidth int
		for j = i; j < n; j++ {
			if curWidth+len(words[j])+j-i > maxWidth {
				break
			}

			curWidth += len(words[j])
		}

		var oneRes string
		if j == n || j == i+1 {
			for k := i; k < j-1; k++ {
				oneRes += words[k] + " "
			}
			oneRes += words[j-1]
			oneRes += getSpace(maxWidth - len(oneRes))
		} else {
			space := maxWidth - curWidth
			ave, remain := space/(j-i-1), space%(j-i-1)
			for k := i; k < j-1; k++ {
				oneRes += words[k]
				if remain > 0 {
					oneRes += getSpace(ave + 1)
					remain--
				} else {
					oneRes += getSpace(ave)
				}
			}
			oneRes += words[j-1]
		}

		res = append(res, oneRes)
		i = j
	}

	return res
}

func getSpace(n int) string {
	var res string
	for i := 0; i < n; i++ {
		res += " "
	}

	return res
}
