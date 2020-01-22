package main

import "strconv"

func addBinary(a string, b string) string {
	var (
		m   = len(a) - 1
		n   = len(b) - 1
		c   int
		res string
	)

	if m < n {
		return addBinary(b, a)
	}

	for m >= 0 && n >= 0 {
		v1, v2 := int(a[m]-'0'), int(b[n]-'0')
		res = strconv.Itoa((v1+v2+c)%2) + res
		c = (v1 + v2 + c) / 2
		m--
		n--
	}

	for m >= 0 {
		v1 := int(a[m] - '0')
		res = strconv.Itoa((v1+c)%2) + res
		c = (v1 + c) / 2
		m--
	}

	if c > 0 {
		res = strconv.Itoa(c) + res
	}

	return res
}
