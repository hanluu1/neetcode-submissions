class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return indices of 2 number sum up to target
        #use a map to store value and index
        keyMap = {}
        #i is index and n is value
        for i, n in enumerate(nums):
            diff = target - n
            if diff in keyMap:
                return [keyMap[diff],i]
            keyMap[n] = i
