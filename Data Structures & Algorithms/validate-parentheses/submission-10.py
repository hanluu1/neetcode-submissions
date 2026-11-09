class Solution:
    def isValid(self, s: str) -> bool:
        matches = {'}' : '{', ']' : '[', ')' : '('}
        stack = []
        for b in s:
            if b in matches:
                if stack and stack[-1] == matches[b]:
                    stack.pop()
                else: return False
            else:
                stack.append(b)
        return True if not stack else False

           