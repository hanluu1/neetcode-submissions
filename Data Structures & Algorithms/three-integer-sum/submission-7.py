class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -(nums[i]) = nums[l] + nums[r]
        # target = 2sum
        nums.sort()
        ans = []
        for i in range(len(nums)):
            #if the smallest number is positive then there no pair will make sum to 0
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return ans

