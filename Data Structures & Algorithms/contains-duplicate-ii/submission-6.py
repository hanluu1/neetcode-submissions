class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = set()
        i = 0
        for j in range(len(nums)):
            if j - i > k:
                store.remove(nums[i])
                i+=1
            if nums[j] in store:
                return True
            store.add(nums[j])
        return False