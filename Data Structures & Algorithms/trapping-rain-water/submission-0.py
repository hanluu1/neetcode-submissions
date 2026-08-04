class Solution:
    def trap(self, height: List[int]) -> int:
        #lam sao de tinh la giu nuoc?
        #next block have to be zero or less than first block and the other block larger to hold water
        if not height: return 0
        
        l, r = 0, len(height) -1
        leftMax, rightMax = height[l], height[r]
        ans = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]
        return ans