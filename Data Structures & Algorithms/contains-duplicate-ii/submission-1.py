class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
         #sliding window 
         #use hash set to keep track the value in nums
         #if there is # in nums that is duplicate within the k window then return true
        mapp = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k: 
                mapp.remove(nums[l])
                l+=1
            if nums[r] in mapp:
                return True
            mapp.add(nums[r])
            
        return False
                