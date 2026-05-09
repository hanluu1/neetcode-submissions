class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #remove duplicate in place
        #if the number appear more than one remove it from map then return k
        #two pointer
        l = 1 #because first number is unique
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:  #pointer move by r so compare number from r and before it 
                nums[l] = nums[r]
                l+=1
            
        return l #because l start at 1 so don't need to plus 1 to get total