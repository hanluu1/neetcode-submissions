class Solution:
    def isValid(self, s: str) -> bool:
        #using stack 
        #if the open parentheses not in stack, append it 
        #if the next parentheses is closed then check if it match with paren in the stack
        #if it does pop the paren out
        #return True if stack not empty

        match = {'}':'{', ']':'[', ')':'('} #store key as closing brackets
        stack = []

        for brackets in s:
            if brackets in match:
                if stack and stack[-1] == match[brackets]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brackets)
        return True if not stack else False
