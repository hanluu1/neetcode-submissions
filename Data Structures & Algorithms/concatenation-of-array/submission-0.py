class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #tao array co len double len array nums, but that array co same number voi arr num
        
        ans1=[]
        ans2=[]
        for i in range(len(nums)):
            ans1.append(nums[i])
            ans2.append(nums[i])
        
        
        return ans1+ans2