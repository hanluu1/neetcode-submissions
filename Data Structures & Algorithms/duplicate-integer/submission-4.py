class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for i, n in enumerate(nums):
            if n in tracker:
                return True
            tracker[n] = True
        return False