class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #return the elements that appears the most in the array
        count = defaultdict(int)
        element = maxCount = 0

        for i in nums:
            count[i] +=1
            if maxCount < count[i]:
                element = i
                maxCount = count[i]
        return element