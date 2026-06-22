class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #if currence sum is less than 0 then curSum set to 0 - reset point and curSum calculate again
        ans = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            ans = max(ans, curSum)
        return ans
