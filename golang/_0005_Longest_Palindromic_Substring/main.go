package main

import (
	"bytes"
	"fmt"
)

// brute force + trim
func longestPalindrome(s string) string {
	if len(s) <= 1 {
		return s
	}

	begin, maxLen, n := 0, 0, len(s)
	for i := 0; i < n; {
		if n-i <= maxLen/2 {
			break
		}

		b, e := i, i
		for e < n-1 && s[e+1] == s[e] {
			e++
		}
		i = e + 1

		for b > 0 && e < n-1 && s[b-1] == s[e+1] {
			b--
			e++
		}

		if e-b+1 > maxLen {
			maxLen = e - b + 1
			begin = b
		}
	}

	return s[begin : begin+maxLen]
}

// Manacher
func longestPalindrome2(s string) string {
	if len(s) <= 1 {
		return s
	}

	str := preprocess(s)
	idx, longest, n := 0, 0, len(str)
	radius := make([]int, n)
	for i := range str {
		r := 1
		if longest > i {
			j := 2*idx - i
			if longest-i > radius[j] {
				r = radius[j]
			} else {
				r = longest - i
			}
		}

		for i-r >= 0 && i+r < n && str[i-r] == str[i+r] {
			r++
		}
		radius[i] = r

		if i+r > longest {
			idx, longest = i, i+r
		}
	}

	idx, maxLen := 0, 0
	for i, r := range radius {
		if r > maxLen {
			idx, maxLen = i, r
		}
	}

	return s[(idx-maxLen+1)/2 : (idx+maxLen-1)/2]
}

func preprocess(s string) string {
	res := bytes.Buffer{}
	for _, c := range s {
		res.WriteByte('#')
		res.WriteByte(byte(c))
	}
	res.WriteByte('#')

	return res.String()
}

func main() {
	fmt.Println(longestPalindrome2("babad"))
}
