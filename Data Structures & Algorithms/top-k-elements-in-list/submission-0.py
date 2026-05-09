class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            count[i] = 1 + count.get(i, 0)
            
        for i, values in count.items():
            freq[values].append(i)
        
        ans = []
        #loop from the bottom to top
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
       
        
