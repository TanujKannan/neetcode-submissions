class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}

        res = []

        for i , ch in enumerate(s):
            last_index[ch] = i
        
        size = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last_index[ch])
            size += 1

            if i == end:
                res.append(size)
                size = 0
                end = 0
    
        return res

        