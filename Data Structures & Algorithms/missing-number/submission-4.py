class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #[1,2,3] [0,2,3]
        ans = len(nums) #3

        for i in range(len(nums)):
            ans += i - nums[i] #2, 1, 0 | 3, 2, 1
        return ans