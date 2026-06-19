class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #get the mid index and use the number at index to compare it with target
        #if target is larger then search right
        #if it smaller then search left
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


