class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(path[:]))
                return

            if openCount < n:
                path.append('(')
                dfs(openCount + 1, closedCount)
                path.pop()

            if closedCount < openCount:
                path.append(')')
                dfs(openCount, closedCount + 1)
                path.pop()

        dfs(0, 0)
        return res        