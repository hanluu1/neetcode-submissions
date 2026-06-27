class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        
        #what the loop will look like
        for i in range(len(nums) - k + 1):
        
        #append max element in the window to ans
            maxVal = nums[i]
            for j in range(i, i + k):
                maxVal= max(maxVal, nums[j])
            ans.append(maxVal)
        return ans


