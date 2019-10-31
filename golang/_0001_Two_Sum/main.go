package main

func twoSum(nums []int, target int) []int {
	idxMap := make(map[int]int, len(nums))
	for i, n := range nums {
		if j, ok := idxMap[target-n]; ok {
			return []int{i, j}
		}

		idxMap[n] = i
	}

	return nil
}
