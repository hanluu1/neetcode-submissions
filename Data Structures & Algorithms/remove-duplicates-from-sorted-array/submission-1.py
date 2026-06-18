class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two pointer
    
        left, right = 0, 0
        while right < len(nums):
            #copy num in right to left so that if it is duplicate we keep the newest num from right
            nums[left] = nums[right]
            while right < len(nums) and nums[left] == nums[right]:
                right +=1
           
            left+=1
              
        return left

