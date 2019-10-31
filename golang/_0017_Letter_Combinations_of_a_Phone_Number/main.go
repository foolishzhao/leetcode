package main

var mp = map[byte]string{
	'2': "abc",
	'3': "def",
	'4': "ghi",
	'5': "jkl",
	'6': "mno",
	'7': "pqrs",
	'8': "tuv",
	'9': "wxyz",
}

func letterCombinations(digits string) []string {
	res, curRes := make([]string, 0), ""
	if len(digits) > 0 {
		dfs(&res, curRes, mp, digits, 0)
	}

	return res
}

func dfs(res *[]string, curRes string, mp map[byte]string, digits string, pos int) {
	if pos == len(digits) {
		*res = append(*res, curRes)
		return
	}

	for _, v := range mp[digits[pos]] {
		dfs(res, curRes+string(v), mp, digits, pos+1)
	}
}
