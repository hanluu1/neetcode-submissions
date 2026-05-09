class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #all indexes have to be different and sum of numbers in those indexes = 0
        ans = []
        nums.sort()
        for i, s in enumerate(nums): #s is value at i in enumerate
            if s > 0:
                break
            if i > 0 and s == nums[i-1]:
                continue
            j = i+1
            k = len(nums) -1
            while j < k:
                if nums[j] + nums[k] < -s:
                    j += 1
                elif nums[j] + nums[k] > -s:
                    k -= 1
                else:
                    ans.append([s, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: #handle duplicate
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -=1
        return ans