'''
Need to insert based on start time (use bisect)
And then merge
Given that initial intervals are all non-overlapping.
So need to consider prior and posterior only?

intervals = [[1,3],[4,6]], new = [2,5]
Based on start time, order would be [1 3], [2 5], [4 6]

Maybe first insert and then second pass to merge intervals?

Two intervals overlap when? [a b] [c d] - [1 6] [2 5]
Need b >= c. Merged interval becomes [a max(b,d)]?

When is it a guaranteed non-issue? b < c
When 

[2 5] [3 6] -> [2 6]

[1 3] [2 5] [4 6]
[1 5] [4 6]
[1 6]
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res



        