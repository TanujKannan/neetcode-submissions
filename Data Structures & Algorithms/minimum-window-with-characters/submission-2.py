'''
given two strings
need to return shortest substring of s such that every char in t, including dups,
is in the substring.

facts:
1. Length of the window must be at least len(t)
2. imagining an accordion. i expand the window till I have everything I need
and then shrink from the left as much as possible and update my shortest substring

Need:
1. To store start and end indices of result substring to recreate at the end.
2. minLen variable used to check if a shorter valid substring has been found.
3. have -> variable to keep track of how many of t's chars are in the window.
4. need -> number of chars in t, including dups?
5. windowCount -> HashMap that stores count of each char in the window
6. needCount -> HashMap that stores count of each char in s

Will return s[start_index:end_index], which will be stored in res.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needCount = Counter(t)
        windowCount = defaultdict(int)

        print(needCount)

        res = [0, 0]

        minLen = float('inf')

        have = 0
        need = len(needCount)
        print("need", need)

        # Sliding window expansion compression logic
        l = 0

        for r in range(len(s)):
            windowCount[s[r]] += 1
            if windowCount[s[r]] == needCount[s[r]]:
                have += 1
                while have == need:
                    if minLen > r - l + 1:
                        res = [l, r]
                        minLen = min(minLen, r - l + 1)
                    #Try shrinking the window from the left
                    windowCount[s[l]] -= 1
                    if windowCount[s[l]] < needCount[s[l]]:
                        have -= 1
                    l += 1

        if minLen == float('inf'):
            return ""
        return s[res[0]: res[1]+1]






        