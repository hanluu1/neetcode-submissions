class Solution:
    def isValid(self, s: str) -> bool:
        match = {")" : "(" , "}" : "{", "]" : "["}
        stack = []
        for i in s:
            #if the bracket in dictionaries we check if it is open bracket or close bracket
            if i in match:
                #if the stack is not empty and the closed bracket match with open bracket we pop that open bracket out to make the stack empty
                if stack and stack[-1] == match[i]:
                    stack.pop()
                #if stack is empty and next bracket is closed then return false because there is no open bracket or nothing to match
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False


