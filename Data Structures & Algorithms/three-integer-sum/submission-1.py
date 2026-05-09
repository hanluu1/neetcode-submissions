class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #ask to return the values sum up to zero
        #sort the array
        nums.sort()
        res = []
        #2 pointers, sum to be zero is sum of left and right equal to negative sum of the other number
        #if sum of 2 number of pointer larger than zero then the other number is close the left side because it has to be negativ
        #else it is close to the right 
        
        for i, a in enumerate(nums):
            if a > 0:
                break #because if a positive at first there is no number to make it to zero because it need to have at least one negative number
            if i > 0 and a == nums[i-1]:
                continue
            left, right= i+1, len(nums) -1
            while left < right:
                total = a + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -=1
                #skip duplicates
                else:
                    res.append([a,nums[left],nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left -1] and left <right:
                        left+=1
        return res


