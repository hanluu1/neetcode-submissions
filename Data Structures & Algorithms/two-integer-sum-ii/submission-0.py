class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #array is already sorted
        #if two pointer one is at beginning one is at the end. 
        #if sum larger than target then decrease right pointer
        #if sum is less than target increase left pointer
        #return sum = target
        left, right = 0, len(numbers) -1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -=1
            elif numbers[left] + numbers[right] < target:
                left +=1
            else: 
                return [left+1,right+1]
        return []