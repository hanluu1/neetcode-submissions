class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #compute the product of nums before the i: prefix
        ans = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            #prefix of first number is 1
            ans[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans



             

        #compute the product of nums after i
        #compute those 2 together will get ans[i]
