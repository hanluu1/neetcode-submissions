class Solution:
    def isPalindrome(self, s: str) -> bool:
         #first thought is solve using 2 pointer
         #return true if read the same forward and backward
         #can solve by reverse a string if the reverse string match with unreverse return true
         #s[::-1] is the reverse string
        
         l = 0
         r = len(s) - 1
         while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
         return True


