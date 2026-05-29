class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash map
        numMap = {}
        for i,c in enumerate(nums):
            if target - c in numMap:
                return [numMap[target-c],i]
            numMap[c] = i