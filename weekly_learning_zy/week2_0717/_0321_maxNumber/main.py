class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def helper(arr, n):
            st = []
            l = len(arr)
            for i , num in enumerate(arr):
                while st and  num > st[-1] and len(st) + l-i+1 >= n:
                    st.pop()
                # 如果没有这一步判断， len(st) + l-i+1是结果集的空位 是很可能大于目前要选择的元素总数n的，
                # 那么很可能就会把之后比当前st[-1]小的值都append进来

                if len(st) < n:
                    st.append(num)

        def merge(arr1, arr2):
            res = []
            while arr1 or arr2:
                if arr1 > arr2:
                    res.append(arr1[0])
                    arr1 = arr1[1:]
                else:
                    res.append(arr2[0])
                    arr2 = arr2[1:]
        res = []
        for u in range(k + 1):
            if u > len(nums1) and k-u > len(nums2):
                continue
            ans1 = helper(nums1,u)
            ans2 = helper(nums2,k-u)

            res = max(res,merge(ans2,ans1))

        return res




