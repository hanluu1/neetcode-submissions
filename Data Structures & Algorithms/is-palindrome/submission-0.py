class Solution:
    def isPalindrome(self, s: str) -> bool:
         #first thought is solve using 2 pointer
         #return true if read the same forward and backward
         #can solve by reverse a string if the reverse string match with unreverse return true
         #s[::-1] is the reverse string
        
         l = 0
         r = len(s) - 1
         while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
         return True


