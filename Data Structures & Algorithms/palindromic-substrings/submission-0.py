class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def expand(i , j):
            left = i
            right = j
            count = 0
            while 0<=left and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        ans = 0
        for i in range(n):
            ans += expand(i , i)
            ans += expand(i , i+1)
        
        return ans
        