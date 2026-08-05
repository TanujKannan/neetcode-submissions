class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def countChars(s):
            counts = [0]*26
            for ch in s:
                index = ord(ch) - ord('a')
                counts[index] += 1
            return tuple(counts)
        
        groupAnagrams = defaultdict(list)

        for s in strs:
            key = countChars(s)
            groupAnagrams[key].append(s)
        
        return list(value for value in groupAnagrams.values())
        