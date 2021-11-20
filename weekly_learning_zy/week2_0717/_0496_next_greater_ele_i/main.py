class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        st = []
        ans = []

        for num in nums2:
            while st and st[-1] < num:
                d[st.pop()] = num
            st.append(num)

        for x in nums1:
            ans.append(d.get(x, -1))

        return ans

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            found = False
            for j in range(nums2.index(num) + 1, len(nums2)):
                if nums2[j] > num:
                    ans.append(nums2[j])
                    found = True
                    break
            if not found:
                ans.append(-1)

        return ans

    class Solution:
        def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            nextGtr, st = dict(), list()
            for i, v in enumerate(nums2):
                while st and st[-1] < v:
                    nextGtr[st.pop()] = v
                st.append(v)

            return [nextGtr.get(x, -1) for x in nums1]