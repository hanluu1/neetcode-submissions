class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's
        ans = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            ans = max(curSum, ans)
        return ans