class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(i , j):
            left = i
            right = j
            while 0<=left and right<n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right - left - 1
        
        ans = [0, 0]

        '''
        s = aabaa
        len = 5. need 0 , 4
        l = 2 - 5//2
        r = 2 + 5//2

        s = aabbaa
        len = 6, need 0, 5
        l = 2 - 6//2 + 1 = 
        r = 2 + 6//2
        '''

        for i in range(n):
            oddLength = expand(i , i)
            if ans[1] - ans[0] + 1 < oddLength:
                ans[0] = i - (oddLength//2)
                ans[1] = i + (oddLength//2)
            
            evenLength = expand(i , i + 1)
            if ans[1] - ans[0] + 1 < evenLength:
                ans[0] = i - (evenLength//2) + 1
                ans[1] = i + (evenLength//2)
        
        return s[ans[0]: ans[1] + 1]
        