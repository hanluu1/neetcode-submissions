class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #three pointers
        
        left, right = 0, len(nums) -1
        i = 0

        while i <= right:
            if nums[i] == 0:
                tmp = nums[i]
                nums[i] = nums[left]
                nums[left] = tmp
                left+=1
            elif nums[i] ==2:
                tmp = nums[i]
                nums[i] = nums[right]
                nums[right] = tmp
                right -=1
                i -=1 #because don't want to pass 2 so have to decrease i
            i+=1

        