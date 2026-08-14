class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
      
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            #left half is sorted so search left 
            if nums[l] <= nums[m]:
                
                if target > nums[l] and target < nums[m]:
                    r = m - 1
                else: l = m + 1
            #right half is sorted so search right
            else:
                if target > nums[m] and target < nums[r]:
                    l = m + 1
                else: r = m - 1
        return -1
            

     
                
