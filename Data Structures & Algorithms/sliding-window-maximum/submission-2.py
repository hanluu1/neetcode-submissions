class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        l = 0
        #mononically decreasing queue
        for r in range(len(nums)):
            #append value to q so that q have value from larger to smaller
            #pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) 

            #remove left from window
            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                ans.append(nums[q[0]])
                l += 1
            
        return ans
