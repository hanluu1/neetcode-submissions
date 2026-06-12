class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer to see if the first char match the last char and continue moving the pointer 
        l = 0
        r = len(s) - 1
        while l < r:
            #check if the char is alphanumeric or not if not skip that 
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False    
                l+=1
                r+=1
        return True