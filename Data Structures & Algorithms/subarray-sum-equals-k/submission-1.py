class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #find contiguos subarray sum up to k
       
        #prefix approach
        #base case is there is a prefix of zero
        ans = 0
        curSum = 0
        prefixSums={0:1} #where 0 is cur sum and 1 is how many time that cursum has appeared

        #loop nums list and get the difference from cursum and k 
        for i in nums:
            curSum += i
            diff= curSum - k
            #the ans will be the total of the diffence from current sum with k
            #that existed in prefixsum
            ans += prefixSums.get(diff, 0)
            #update prefixSums 
            prefixSums[curSum] = 1 + prefixSums.get(curSum,0)
        return ans


