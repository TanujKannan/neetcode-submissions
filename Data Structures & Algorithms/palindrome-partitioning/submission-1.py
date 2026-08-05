class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []
        def isPalindrome(s):
            return s == s[::-1]
        
        def dfs(start):
            if start == n:
                res.append(path[:])
            
            for i in range(start, n):
                substring = s[start: i + 1]
                if isPalindrome(substring):
                    path.append(substring)
                    dfs(i + 1)
                    path.pop()
        
        dfs(0)
        return res
        