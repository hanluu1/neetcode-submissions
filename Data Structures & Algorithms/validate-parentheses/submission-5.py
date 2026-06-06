class Solution:
    def isValid(self, s: str) -> bool:
        #having list matching bracket
        matchBrackets = {')':'(', ']':'[', '}': '{'}
        stack = []
        for b in s:
            if b in matchBrackets:
                #the most recent bracket match the open bracket so pop open bracket out
                if stack and stack[-1] == matchBrackets[b]:
                    stack.pop() 
                else:
                    return False #return false when no matching
            else: stack.append(b) #append open bracket 
        #goal to be true when stack is empty
        return True if not stack else False

            
