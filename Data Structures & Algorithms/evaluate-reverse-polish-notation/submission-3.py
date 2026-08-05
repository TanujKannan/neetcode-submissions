class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops ={'+', '-', '/', '*'}

        stack = []

        for token in tokens:
            if token in ops:
                if token == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                elif token == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                elif token == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif token == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(float(b / a)))
            else:
                stack.append(int(token))
        
        return stack[0]
        