package main

// time complexity O(log(m+n)), space complexity O(1)
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	m, n := len(nums1), len(nums2)
	k := (m + n) / 2

	if (m+n)%2 == 1 {
		return float64(helper(nums1, 0, m, nums2, 0, n, k+1))
	} else {
		return float64(helper(nums1, 0, m, nums2, 0, n, k) +
			helper(nums1, 0, m, nums2, 0, n, k+1)) / 2
	}
}

func helper(nums1 []int, s1, m int, nums2 []int, s2, n, k int) int {
	if m > n {
		return helper(nums2, s2, n, nums1, s1, m, k)
	} else if m == 0 {
		return nums2[s2+k-1]
	} else if k == 1 {
		if nums1[s1] < nums2[s2] {
			return nums1[s1]
		} else {
			return nums2[s2]
		}
	}

	p1 := k >> 1
	if p1 > m {
		p1 = m
	}

	p2 := k - p1

	if nums1[s1+p1-1] == nums2[s2+p2-1] {
		return nums1[s1+p1-1]
	} else if nums1[s1+p1-1] > nums2[s2+p2-1] {
		return helper(nums1, s1, p1, nums2, s2+p2, n-p2, p1)
	} else {
		return helper(nums1, s1+p1, m-p1, nums2, s2, p2, p2)
	}
}

// time complexity O(m+n), space complexity O(m+n)
func findMedianSortedArrays2(nums1 []int, nums2 []int) float64 {
	nums3 := merge(nums1, nums2)
	n := len(nums3)

	if (n % 2) == 1 {
		return float64(nums3[n/2])
	} else {
		return float64(nums3[n/2]+nums3[n/2-1]) / 2
	}
}

func merge(nums1 []int, nums2 []int) []int {
	m, n, i, j, k := len(nums1), len(nums2), 0, 0, 0
	nums3 := make([]int, m+n)

	for i < m && j < n {
		if nums1[i] < nums2[j] {
			nums3[k] = nums1[i]
			i++
		} else {
			nums3[k] = nums2[j]
			j++
		}
		k++
	}

	for i < m {
		nums3[k] = nums1[i]
		i++
		k++
	}

	for j < n {
		nums3[k] = nums2[j]
		j++
		k++
	}

	return nums3
}
