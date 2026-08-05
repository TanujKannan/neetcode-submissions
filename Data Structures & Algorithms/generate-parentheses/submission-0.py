class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []

        def recurse(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(path[:]))
                return
            
            if openCount < n:
                path.append('(')
                recurse(openCount+1, closedCount)
                path.pop()
        
            if closedCount < openCount:
                path.append(')')
                recurse(openCount, closedCount + 1)
                path.pop()

        recurse(0, 0)
        return res        