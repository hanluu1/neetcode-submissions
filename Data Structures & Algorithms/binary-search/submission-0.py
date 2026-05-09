class Solution:
    def search(self, nums: List[int], target: int) -> int:
         #binary search is the method that you take the middle 
         #point and compare it to the left and right of nums
         #if mid < target then position is from mid to right
         #elif mid > target then pos is from left to mid
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1




         