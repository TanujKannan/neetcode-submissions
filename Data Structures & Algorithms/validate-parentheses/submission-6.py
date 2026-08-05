class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in paren:
                if stack and stack[-1] == paren[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        print(stack)
        return len(stack) == 0
        