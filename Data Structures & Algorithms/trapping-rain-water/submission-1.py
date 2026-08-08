class Solution:
    def trap(self, height: List[int]) -> int:
        #left and right compare to current position of the heigt
        if not height: 
            return 0
        l = 0
        r = len(height) - 1
        maxArea = 0

        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                maxArea += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                maxArea += rightMax - height[r]
        return maxArea

           


        