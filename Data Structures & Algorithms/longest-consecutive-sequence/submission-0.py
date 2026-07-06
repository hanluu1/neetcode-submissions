class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        #return the longest len of consecutive number in the array

        if not nums:
            return 0
        ans = 1
        count = 1
        for i in range(1, len(nums)):
            #if the next number > than the curr more than 1
            if nums[i] == nums[i-1]:
                continue
            if nums[i] - nums[i-1] == 1:
                count += 1
                
            else: 
                count = 1

            ans = max(ans, count)
        return ans
                

