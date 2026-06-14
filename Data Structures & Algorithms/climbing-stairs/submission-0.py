class Solution:
    def climbStairs(self, n: int) -> int:
        #bottom up
        #2 ways to step 1 step or 2 steps to get to nth steps
        one, two = 1, 2

        if n <= 2:
            return n

        for i in range(3, n + 1):
            one, two = two, one + two
        return two