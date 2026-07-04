class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = count = 0
        for i in nums:
            if i == 0:
                ans = max(ans, count)
                count = 0
            else:
                count += 1
        return max(count, ans)
                