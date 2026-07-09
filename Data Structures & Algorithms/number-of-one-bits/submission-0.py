class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            #check if n is 1 if it is 1 add to ans then shift n to the right
            ans += n % 2
            n = n >> 1
        return ans
       