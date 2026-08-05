class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}

        for token in tokens:
            if token in ops:
                if token == '+':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a + b)
                elif token == '*':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a * b)
                elif token == '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b - a)
                
                elif token == '/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        
        return stack[0]

        