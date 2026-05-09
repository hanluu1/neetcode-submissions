class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #have a map to save the items if items appear again then return True
        map = {}
        for i,n in enumerate(nums):
            if n in map:
                return True
            map[n] = True
        return False