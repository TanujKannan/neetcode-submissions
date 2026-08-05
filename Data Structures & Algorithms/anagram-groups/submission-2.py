'''
Given a list of strings, need to group anagrams together into sublists.
Answer can be returned in any order.

Can create tuples of the char arrays and hash based on that.
So dictionary stores [hashed_tuple, list of strings with that tuple]

At end, return as a list of lists.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_to_strings = {}

        for word in strs:
            charCount = [0]*26
            for ch in word:
                charCount[ord(ch) - ord('a')] += 1
            hashed_arr = tuple(charCount)
            if hashed_arr in tuple_to_strings:
                tuple_to_strings[hashed_arr].append(word)
            else:
                tuple_to_strings[hashed_arr] = []
                tuple_to_strings[hashed_arr].append(word)
        
        res = []
        for tup, list_of_strings in tuple_to_strings.items():
            res.append(list_of_strings)
        
        return res
