package main

import "strings"

func isNumber(s string) bool {
	s = strings.TrimSpace(s)

	var sign, num, dot, exp bool
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c == '+' || c == '-' {
			if sign || num || dot {
				return false
			}
			sign = true
		} else if c >= '0' && c <= '9' {
			num = true
		} else if c == '.' {
			if dot || exp {
				return false
			}
			dot = true
		} else if c == 'e' {
			if exp || !num {
				return false
			}
			exp = true
			num = false
			sign = false
			dot = false
		} else {
			return false
		}
	}

	return num
}
