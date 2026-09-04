class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numSet = set(nums)
        for i in nums:
            if i - 1 not in numSet:
                length = 0
                while i + length in numSet:
                    length += 1
                ans = max(ans, length)
        return ans
