class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        need = len(countT)
        have = 0

        res = [-1, -1]

        l = 0

        windowFreq = defaultdict(int)

        min_len = float('inf')

        for r in range(len(s)):
            windowFreq[s[r]] += 1
            if s[r] in countT and windowFreq[s[r]] == countT[s[r]]:
                have += 1
                while have == need:
                    if r - l + 1 < min_len:
                        min_len = r - l + 1
                        res = [l , r]
                    windowFreq[s[l]] -= 1
                    if s[l] in countT and windowFreq[s[l]] < countT[s[l]]:
                        have -= 1
                    l += 1
        
        return s[res[0]: res[1] + 1]


        