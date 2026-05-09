class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #tao array co len double len array nums, but that array co same number voi arr num
        
        ans = [0] * (2*len(nums))
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans