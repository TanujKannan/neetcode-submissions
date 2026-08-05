class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        windowCount = defaultdict(int)

        l = 0
        ans = [-1, -1]
        have = 0
        need = len(countT)
        min_len = float('inf')

        for r in range(len(s)):
            windowCount[s[r]] += 1
            if s[r] in countT and windowCount[s[r]] == countT[s[r]]:
                have += 1
                while have == need:
                    if r - l + 1 < min_len:
                        min_len = r - l + 1
                        ans = [l , r]
                    windowCount[s[l]] -= 1
                    if s[l] in countT and windowCount[s[l]] < countT[s[l]]:
                        have -= 1
                    
                    l += 1
    
        return s[ans[0]: ans[1]+1]

        