package main

func restoreIpAddresses(s string) []string {
	res := make([]string, 0)
	if len(s) < 4 && len(s) > 12 {
		return res
	}

	dfs(&res, "", s, 0, 0)
	return res
}

func dfs(res *[]string, oneRes, s string, pos, times int) {
	if times == 4 && pos == len(s) {
		*res = append(*res, oneRes[:(len(oneRes) - 1)])
		return
	} else if times == 4 || pos == len(s) {
		return
	}

	c := s[pos]
	dfs(res, oneRes+string(c)+".", s, pos+1, times+1)
	if pos < (len(s)-1) && c != '0' {
		dfs(res, oneRes+s[pos:pos+2]+".", s, pos+2, times+1)
	}
	if pos < (len(s)-2) && (c == '1' || (c == '2' && (s[pos+1] < '5' || (s[pos+1] == '5' && s[pos+2] < '6')))) {
		dfs(res, oneRes+s[pos:pos+3]+".", s, pos+3, times+1)
	}
}
