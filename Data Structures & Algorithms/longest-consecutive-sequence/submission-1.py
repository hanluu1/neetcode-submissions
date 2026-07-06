class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hash set 
        numSet = set(nums)
        ans = 0
        
        for n in numSet:
            if n - 1 not in numSet:
                count = 1
                while n + count in numSet:
                    count += 1
            ans = max(ans, count)
        return ans
