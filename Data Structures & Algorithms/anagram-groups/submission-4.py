'''
Given a list of strings, need to group anagrams together into sublists.
Answer can be returned in any order.

Can create tuples of the char arrays and hash based on that.
So dictionary stores [hashed_tuple, list of strings with that tuple]

At end, return as a list of lists.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_to_strings = defaultdict(list)

        for word in strs:
            charCount = [0]*26
            for ch in word:
                charCount[ord(ch) - ord('a')] += 1
            hashed_arr = tuple(charCount)
            tuple_to_strings[hashed_arr].append(word)
    
        
        return list(tuple_to_strings.values())
