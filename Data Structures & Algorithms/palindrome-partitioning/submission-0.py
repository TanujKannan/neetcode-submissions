class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def isPalindrome(p):
            return p == p[::-1]
        
        path = []
        res = []

        def recurse(start):
            if start == n:
                res.append(path[:])
                return
            
            for j in range(start, n):
                if isPalindrome(s[start:j+1]):
                    path.append(s[start:j+1])
                    recurse(j+1)
                    path.pop()
        
        recurse(0)
        return res
