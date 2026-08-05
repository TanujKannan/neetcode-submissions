class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        left = [-1]*n
        right = [n]*n


        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []

        for i in range(n-1, -1 , -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        

        max_rectangle = 0

        for i in range(n):
            max_rectangle = max(max_rectangle, (right[i]-left[i]-1)*heights[i])
        
        return max_rectangle
            