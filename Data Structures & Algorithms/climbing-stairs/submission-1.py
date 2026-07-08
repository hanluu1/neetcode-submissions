class Solution:
    def climbStairs(self, n: int) -> int:
        #how many ways to climb on the top of the stair with either 1 or 2 steps at time
        prev, curr = 1, 2
    
        if n <= 2:
            return n
        
        #start from step 3
        for i in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr
