class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       #remove val in nums inplace
       #return k total number of element left after remove val
       #two pointer to swap element
       i = 0
       n = len(nums)
       while i < n:
        if nums[i] == val:
            n-=1        #length decrease by 1
            nums[i] = nums[n] #swap val in current i to n
        else: 
            i +=1
       return n 



            
                
        