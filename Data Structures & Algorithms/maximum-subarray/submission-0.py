class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #brute force:
        ans = nums[0]
        for i in range(len(nums)):
            curSum = 0
            for j in range(i,len(nums)):
                curSum += nums[j]
                ans = max(ans, curSum)
        return ans
                