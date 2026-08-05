'''
Need to encode a list of strings into a single string.

Need to also be able to decode an encoded string back into a list of strings.

To be able to decode a string back into a list, what do I need to know?
1. Need to know the boundaries of each word.
    -> I need to know the length of each word and where it starts and ends within the encoded string, so I can extract properly.

Which means during encoding I need to store the length of each word, as a hint during decoding so I know the boundaries.

Plan:
Encode so that looks like: wordOne#7wordTwo#9wordThree
Use – as a delimiter.

how would I decode wordOne#7wordTwo#9wordThree

Two pointers l and r. Both start at 0.
Push r till you hit a delimiter. Then s[l:r] is a word.
Then len of next word is at r + 1.
So put l = r and r = l + s[len_next_word]
'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "–" + word
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "–":
                j += 1
            
            len_word = int(s[i: j])

            word_start = j + 1
            word_end = word_start + len_word

            res.append(s[word_start: word_end])

            i = word_end
        return res


