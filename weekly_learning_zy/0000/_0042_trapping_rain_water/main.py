class Solution:
    def trap(self, height: List[int]) -> int:
        LeftMaxIncludingCurrent = [0] * len(height)
        # Array that stores largest element to itself in right
        RightMaxIncludingCurrent = [0] * len(height)
        # This is just for simplicity, you actually don't need it, just take some counter over here
        Water = [0] * len(height)

        maxLeft = 0
        maxRight = 0

        # Fill up the LeftMaxIncludingCurrent Array
        for index in range(len(height)):
            maxLeft = max(maxLeft, height[index])
            LeftMaxIncludingCurrent[index] = maxLeft
        # Fill up the RightMaxIncludingCurrent Array
        for index in range(len(height) - 1, -1, -1):
            maxRight = max(maxRight, height[index])
            RightMaxIncludingCurrent[index] = maxRight

        # Find the height of the water as discussed above in the concept
        for index in range(len(height)):
            Water[index] = min(LeftMaxIncludingCurrent[index], RightMaxIncludingCurrent[index]) - height[index]
        # Take the sum of water that accumulated above every other building to get total water that got accumulated.
        return sum(Water)


        leftmaxarr = [0]*len(height)
        rightmaxarr = [0]*len(height)
        leftmax = 0
        rightmax = 0
        ans = [0]*len(height)
        for i in range (len(height)):
            leftmax = max(leftmax ,height[i])
            leftmaxarr[i] = leftmax
        for j in range(len(height)-1,-1,-1):
            rightmax = max(rightmax,height[j])
            rightmaxarr[j] = rightmax

        for p in range(len(height)):
            ans[p] = min(leftmaxarr[p],rightmaxarr[p])-height[p]

