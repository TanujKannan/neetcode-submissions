class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        path = []
        res = set()

        def recurse(start, remaining):
            if remaining == 0:
                res.add(tuple(path[:]))
                return
            
            for i in range(start,n):
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])

                recurse(i + 1, remaining - candidates[i])

                path.pop()

        recurse(0 , target) 
        return list(list(tup) for tup in res)   