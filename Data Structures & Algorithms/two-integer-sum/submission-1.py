class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target - nums[i] = difference
        #if difference in the map then return 
        seen = {}
        #i index n values
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff],i] #diff is the value of the index that found in seen
            seen[n] = i 
            
        
