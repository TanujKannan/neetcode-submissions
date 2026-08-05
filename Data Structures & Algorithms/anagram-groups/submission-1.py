class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def countChars(s):
            counts = [0]*26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            return tuple(counts)
        
        groupByCounts = defaultdict(list)

        for s in strs:
            key = countChars(s)

            groupByCounts[key].append(s)
    
        return list(groupByCounts.values())
        