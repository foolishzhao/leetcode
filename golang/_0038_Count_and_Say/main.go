package main

import "strconv"

func countAndSay(n int) string {
	res := "1"
	for i := 1; i < n; i++ {
		res = getNext(res)
	}

	return res
}

func getNext(str string) string {
	res := ""

	i, j, n := 0, 1, len(str)
	for j < n {
		if str[j] == str[i] {
			j++
		} else {
			res += strconv.Itoa(j-i) + string(str[i])
			i = j
			j = i + 1
		}
	}

	return res + strconv.Itoa(j-i) + string(str[i])
}
