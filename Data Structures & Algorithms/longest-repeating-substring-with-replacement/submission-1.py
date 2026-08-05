class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowFreq = defaultdict(int)
        maxFreq = 0
        l = 0
        longest = 0

        for r in range(len(s)):
            windowFreq[s[r]] += 1
            maxFreq = max(maxFreq, windowFreq[s[r]])
            while (r - l + 1) - maxFreq > k:
                windowFreq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest




        