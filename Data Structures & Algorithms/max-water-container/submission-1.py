class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #amount of water = h x w
        #height = the min height of 2 bars
        #width is the distance between 2 chosen bars
        #how we determine the bar so we get the max amount of water
        #two pointer start at the beginning and one at end
        #calculat the amount, update max 
        #move the pointer that have smaller height
        l = 0
        r = len(heights) - 1
        maxSwater = 0
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            S_water = w * h
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            maxSwater = max(maxSwater, S_water)
        return maxSwater
            

            
    
        

