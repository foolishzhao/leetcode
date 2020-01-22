package main

import "strings"

func simplifyPath(path string) string {
	resArr := make([]string, 0)
	for _, v := range strings.Split(path, "/") {
		if v == "." || v == "" {
			continue
		} else if v == ".." {
			if len(resArr) > 0 {
				resArr = resArr[:len(resArr)-1]
			}
		} else {
			t := v
			resArr = append(resArr, t)
		}
	}

	return "/" + strings.Join(resArr, "/")
}
