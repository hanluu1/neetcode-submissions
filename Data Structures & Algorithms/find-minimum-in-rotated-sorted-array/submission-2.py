class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search
        l = 0
        r = len(nums) - 1
        while l < r:
            m = r - (r-l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]


