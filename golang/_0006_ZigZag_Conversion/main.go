package main

import (
	"bytes"
	"strings"
)

func convert(s string, numRows int) string {
	rows := make([]string, numRows)
	for i := 0; i < numRows; i++ {
		rows[i] = ""
	}

	i, n := 0, len(s)
	for i < n {
		for j := 0; j < numRows && i < n; j++ {
			rows[j] += string(s[i])
			i++
		}

		for j := numRows - 2; j > 0 && i < n; j-- {
			rows[j] += string(s[i])
			i++
		}
	}

	return strings.Join(rows, "")
}

// time and space are both worse than solution 1
func convert2(s string, numRows int) string {
	rows := make([]bytes.Buffer, numRows)
	for i := 0; i < numRows; i++ {
		rows[i] = bytes.Buffer{}
	}

	i, n := 0, len(s)
	for i < n {
		for j := 0; j < numRows && i < n; j++ {
			rows[j].WriteByte(s[i])
			i++
		}

		for j := numRows - 2; j > 0 && i < n; j-- {
			rows[j].WriteByte(s[i])
			i++
		}
	}

	res := ""
	for _, v := range rows {
		res += v.String()
	}
	return res
}

// time and space are both worse than solution 1
func convert3(s string, numRows int) string {
	rows := make([][]byte, numRows)
	for i := 0; i < numRows; i++ {
		rows[i] = make([]byte, 0)
	}

	i, n := 0, len(s)
	for i < n {
		for j := 0; j < numRows && i < n; j++ {
			rows[j] = append(rows[j], s[i])
			i++
		}

		for j := numRows - 2; j > 0 && i < n; j-- {
			rows[j] = append(rows[j], s[i])
			i++
		}
	}

	res := ""
	for _, v := range rows {
		res += string(v)
	}
	return res
}
