class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the array is rotated, find the min in array
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return nums[right]
            


