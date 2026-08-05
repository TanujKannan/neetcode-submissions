class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0]*n

        stack = []

        for i , temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                index, _ = stack.pop()
                output[index] = i - index
            stack.append((i, temp))   


        return output     