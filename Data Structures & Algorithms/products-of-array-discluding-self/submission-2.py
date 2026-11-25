class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #calculate the production then divide by i number
        #what if there is zero, because divide to zero giving error
        #anything times zero is zero
        #if zero > 1 then init array with all zero

        
        prod = 1
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        
        ans = [0] * len(nums)
        for i in range(len(nums)):
            
            if zero_count:
                if nums[i] == 0:
                    ans[i] = prod
                else:
                    ans[i] = 0 
            else:
                
                ans[i] = prod // nums[i]

        return ans


                
        


