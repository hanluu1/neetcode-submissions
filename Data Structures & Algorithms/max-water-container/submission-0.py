class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #length or height of index i rep. as heights[i]
        #return the maximum amount of water that form by any 2 bars
        #amount of water = min height of 2 bars x range index between 2 bar

        ans = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            amount_water = (r - l) * min(heights[l], heights[r])
            if heights[l] < heights[r]:
                l += 1
            else: r -= 1
            ans = max(ans, amount_water)
        return ans
