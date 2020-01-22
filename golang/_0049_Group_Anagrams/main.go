package main

import "sort"

func groupAnagrams(strs []string) [][]string {
	anagramMap := make(map[string][]string)
	for i, v := range strs {
		sortedV := sortStr(v)
		anagramMap[sortedV] = append(anagramMap[sortedV], strs[i])
	}

	res := make([][]string, 0, len(anagramMap))
	for k := range anagramMap {
		res = append(res, anagramMap[k])
	}

	return res
}

func sortStr(str string) string {
	byteArr := []byte(str)
	sort.Slice(byteArr, func(i, j int) bool {
		return byteArr[i] < byteArr[j]
	})

	return string(byteArr)
}
