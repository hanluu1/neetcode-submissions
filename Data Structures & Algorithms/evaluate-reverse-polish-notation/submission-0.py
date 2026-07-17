class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        #if it is number append it to stack
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
        
        #when it is operators
            else:
                #pop 2 number before it out then solve it with operators
                #push the ans back to stack
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '*':
                    stack.append(b * a)
                elif token == '-':
                    stack.append(b - a)
                else:
                    stack.append(int(b / a))
        return stack[0]

    

