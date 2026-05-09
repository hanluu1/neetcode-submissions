class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #store openning brackets
        brackets = { ')' : '(', ']':'[', '}':'{' }
        #iterate the characters in string s
        for i in s:
        
            if i in brackets:
        #closing brackets if stack not empty and check if the before bracket match its 
        #pop the closing brackets if match
                if stack and stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    # else return false
                    return False
            else:
            #openning brackets get push to stack
                stack.append(i)
        return True if not stack else False
        
        

        