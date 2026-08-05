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
            #If it's before the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            #If it's after the current interval
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            #If it overlaps, handle it.
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        #If it goes all the way to the end.
        res.append(newInterval)
        return res



        