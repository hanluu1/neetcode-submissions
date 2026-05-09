class Solution:
    def validPalindrome(self, s: str) -> bool:
        #2 pointer to check the string
        def palindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        left = 0
        right = len(s) - 1
        #check the string when deleting at most one char
        while left < right:
            if s[left] != s[right]:
                return (palindrome(left +1, right) 
                    or palindrome(left, right-1))
            left +=1
            right -=1

        return True
            
