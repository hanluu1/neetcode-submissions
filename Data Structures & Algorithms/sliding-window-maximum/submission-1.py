class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #using deque for optimization
        #store the indices in the queue
        #max value at the top of deque, 
        #remove smaller elements from back

        ans = []
        dq = deque()
        l = 0

        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            #remove front if it outside of window
            if dq[0] < l:
                dq.popleft()
        
            #check if window is at least size k, record max
            if r >= k - 1:
                ans.append(nums[dq[0]])
                l += 1
        return ans

                 



