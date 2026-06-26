class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub = {}
        #key is nums and value is index because we need to return index
        for i,n in enumerate(nums):
            diff = target - n
            if diff in sub:
                return [sub[diff],i]
            sub[n] = i
      